pattern_list = [["###", "  #", "###", "###", "# #", "###", "###", "###", "###", "###"],
                ["# #", "  #", "  #", "  #", "# #", "#  ", "#  ", "  #", "# #", "# #"],
                ["# #", "  #", "###", "###", "###", "###", "###", "  #", "###", "###"],
                ["# #", "  #", "#  ", "  #", "  #", "  #", "# #", "  #", "# #", "  #"],
                ["###", "  #", "###", "###", "  #", "###", "###", "  #", "###", "  #"]]

def main():
    while True:
        try: 
            number_s = str(input("Introduzca un valor: "))
            for r in range(5):
                for i in number_s:
                    i = int(i)
                    print(pattern_list[r][i], end=" ")
                print("")
        except ValueError:
            continue
        except TypeError:
            continue
        except KeyboardInterrupt:
            break

main()