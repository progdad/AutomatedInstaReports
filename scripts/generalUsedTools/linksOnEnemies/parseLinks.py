class LinksSetUp:
    all_needed_domains = [
        "https://www.instagram.com/",
        "https://twitter.com",
        "https://www.youtube.com",
        "t.me",
    ]

    def __init__(self, file, domain):
        self.file = file
        self.domain = domain

    def sort_and_get_pigs(self):
        print(
            "    1.1) Getting all the links of instagram accounts from the file where are all accounts of all social medias:")
        all_links_from_domain = self.__get_the_needed_links()
        print("    1.2) Opening file with already reported users:")

        with open(self.file, "r") as already_reported_file:
            already_reported = already_reported_file.read().split()
        print("    1.3) Deleting already reported users from the future reported users list.")

        for link in already_reported:
            if link in all_links_from_domain:
                pop_index = all_links_from_domain.index(link)
                all_links_from_domain.pop(pop_index)
        return all_links_from_domain

    def __get_the_needed_links(self):
        print(f"        1.1.1) Trying to parse all the links(not only from {self.domain}) from the file:")
        self.__parse()
        print("        1.1.2) Opening the file with all the parsed links.")
        with open("../generalUsedTools/linksOnEnemies/allParsedLinks.txt", "r") as all_links_file:
            print(f"        1.1.3) Sorting and saving only {self.domain} links.")
            return [link for link in all_links_file.read().split() if self.domain in link]

    def __parse(self):
        all_links = []
        print("            1.1.1.1) Open the unparsed file full of junk and get all the links of all accounts.")
        with open("../generalUsedTools/linksOnEnemies/unparsedLinks", "r") as text:
            for string in text.read().split():
                string = string.replace("➡️", "")
                for domain in self.all_needed_domains:
                    if (domain in string) and (string not in all_links):
                        all_links.append(string.strip())
                        break
        print(f"            1.1.1.2) All the {len(all_links)} links are read from file and saved to the list variable.")
        try:
            print("            1.1.1.3) Trying to open the common file with all the links of the all social medias that are already saved")
            with open("../generalUsedTools/linksOnEnemies/allParsedLinks.txt", "r") as links_file:
                enemies_links = links_file.read().split()
                print("            1.1.1.4) The file has been opened and read successfully.")
        except FileNotFoundError:
            print("            1.1.1.4) There is no such file yet. Looks like this is your first program using.")
            enemies_links = []
        finally:
            print("            1.1.1.5) Open file where we save all the parsed links(unique only).")
            with open("../generalUsedTools/linksOnEnemies/allParsedLinks.txt", "a") as links_file:
                for link in all_links:
                    if link not in enemies_links:
                        links_file.write(link + '\n')
            print(f"            1.1.1.6) All the {len(all_links)} links are saved successfully to the file.")

