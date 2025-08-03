#!/usr/bin/env python3

# SpiderFoot API Script para iniciar un escaneo y exportar resultados a CSV.


import requests
import time
import json
import csv
import sys
import argparse

def get_api_key():
    try:
        with open("config.json", "r") as f:
            config = json.load(f)
            return config["api_key"]
    except (FileNotFoundError, KeyError):
        print("Error: Archivo 'config.json' no encontrado o clave 'api_key' inválida.")
        sys.exit(1)

def start_scan(api_url, api_key, scan_name, target, modules):
    # Inicia un scan con los módulos especificados
    url = f"{api_url}/api/scan/start"
    headers = {"X-Api-Key": api_key}
    data = {
        "scan_name": scan_name,
        "target": target,
        "modules": modules
    }
    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()
        return response.json().get("scan_id")
    except requests.RequestException as e:
        print(f"Error al iniciar el scan: {e}")
        sys.exit(1)

def check_scan_status(api_url, api_key, scan_id):
    # Monitorea el estado del scan hasta que termine
    url = f"{api_url}/api/scan/{scan_id}/status"
    headers = {"X-Api-Key": api_key}
    while True:
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            status = response.json().get("status")
            print(f"Estado del scan: {status}")
            if status in ["FINISHED", "ERROR"]:
                return status
            time.sleep(10)  # Espera 10 segundos antes de verificar nuevamente
        except requests.RequestException as e:
            print(f"Error al verificar estado: {e}")
            sys.exit(1)

def get_scan_results(api_url, api_key, scan_id):
    # Recupera los resultados del scan
    url = f"{api_url}/api/scan/{scan_id}/results"
    headers = {"X-Api-Key": api_key}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json().get("data", [])
    except requests.RequestException as e:
        print(f"Error al obtener resultados: {e}")
        sys.exit(1)

def save_results_to_csv(results, output_file):
    # Guarda los resultados en archivo csv
    if not results:
        print("No se encontraron resultados para guardar.")
        return
    with open(output_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Source", "Type", "Data"])  # Encabezados del csv
        for result in results:
            writer.writerow([result.get("source", ""), result.get("type", ""), result.get("data", "")])
    print(f"Resultados guardados en {output_file}")

def main():
    parser = argparse.ArgumentParser(description="Script para automatizar escaneos de SpiderFoot a través de la API.")
    parser.add_argument("--target", default="dominio.com", help="Objetivo del escaneo (dominio, IP, etc.)")
    parser.add_argument("--scan-name", default="test_scan", help="Nombre del scan")
    parser.add_argument("--modules", default="sfp_dnsresolve,sfp_whois,sfp_spider", help="Módulos separados por comas")
    parser.add_argument("--output", default="output.csv", help="Archivo CSV de salida")
    parser.add_argument("--api-url", default="http://127.0.0.1:5001", help="URL del servidor SpiderFoot")
    args = parser.parse_args()

    api_key = get_api_key()
    if not api_key:
        print("Error: Se debe configurar una clave API en SpiderFoot.")
        sys.exit(1)

    # Iniciar el scan
    scan_id = start_scan(args.api_url, api_key, args.scan_name, args.target, args.modules)
    print(f"Scan iniciado con ID: {scan_id}")

    # Monitorear el estado
    status = check_scan_status(args.api_url, api_key, scan_id)
    if status != "FINISHED":
        print(f"El scan terminó con estado: {status}")
        sys.exit(1)

    # Obtener y guardar resultados
    results = get_scan_results(args.api_url, api_key, scan_id)
    save_results_to_csv(results, args.output)

if __name__ == "__main__":
    main()