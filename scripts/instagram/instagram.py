import datetime
import os
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from scripts.generalUsedTools.linksOnEnemies.parseLinks import LinksSetUp
from scripts.generalUsedTools.generalAutomationTools import BaseAutomationTools


begin = datetime.datetime.now()

print("1. GETTING ALL THE INSTAGRAM ACCOUNTS OF THE RUSSIAN ASSHOLES FROM THE FILE:")
setUpLinksInstance = LinksSetUp(file="reportedOnesInst.txt", domain="instagram.com")
INTRUDERS = setUpLinksInstance.sort_and_get_pigs()
print(f"ALL THE PIGS ARE READ FROM THE FILE. THERE ARE {len(INTRUDERS)} Пєтухов Рускава Міра.\n")


class InstagramReport(BaseAutomationTools):
    def __init__(self):
        from __init__ import username, password
        self.username = username
        self.password = password

        self.__reported_pigs = []

        super().__init__()

    def __save_reported_pigs(self):
        print("    13.1) Opening file for the saving with the \"a\" mode:.")
        with open("reportedOnesInst.txt", "a") as reported_pigs_file:
            for pig in self.__reported_pigs:
                ### Log info for standard output.
                pig_index = self.__reported_pigs.index(pig) + 1
                pig_account = pig.split('/')[-2]
                ###
                reported_pigs_file.write(pig + '\n')
                ###
                print(f"        13.1.{pig_index}) @{pig_account} was saved to the file.")
            print(f"{len(self.__reported_pigs)} intruders are saved to the file.")

    def __insta_report(self):
        for intruder in INTRUDERS:
            ### Log info for standard output.
            intruder_account = intruder.split('/')[-2]
            intruder_index = INTRUDERS.index(intruder) + 1
            print(f"    11.{intruder_index}.1) Loading page of this bi*ch >>> @{intruder_account}")
            ###
            self.safe_get(intruder)
            print(f"    11.{intruder_index}.2) Starting REPORT:")
            time.sleep(3.0)
            try:
                print(f"        11.{intruder_index}.2.1) Clicking \"three points\" field near the \"Follow\" button.")
                self.element_existence(
                    elementloc='//*[@id="react-root"]/section/main/div/header/section/div[1]/div/button',
                    findBy=By.XPATH,
                    condition=expected_conditions.element_to_be_clickable
                ).click()
                time.sleep(1.5)
                print(f"        11.{intruder_index}.2.2) Clicking the \"Report\" button.")
                self.element_existence(
                    elementloc="body > div.RnEpo.Yx5HN > div > div > div > div > button:nth-child(3)",
                    findBy=By.CSS_SELECTOR,
                    condition=expected_conditions.element_to_be_clickable
                ).click()
                time.sleep(1.5)
                print(f"        11.{intruder_index}.2.3) Clicking \"Report Account\".")
                self.element_existence(
                    elementloc="/html/body/div[6]/div/div/div/div[2]/div/div/div/div[3]/button[2]",
                    findBy=By.XPATH,
                    condition=expected_conditions.element_to_be_clickable
                ).click()
                time.sleep(1.5)
                print(f"        11.{intruder_index}.2.4) Clicking \"It's posting content that shouldn't be on Instagram\".")
                self.element_existence(
                    elementloc='/html/body/div[6]/div/div/div/div[2]/div/div/div/div[3]/button[1]',
                    findBy=By.XPATH,
                    condition=expected_conditions.element_to_be_clickable
                ).click()
                time.sleep(1.5)
                print(f"        11.{intruder_index}.2.5) Clicking \"Violence or dangerous organizations\".")
                self.element_existence(
                    elementloc='/html/body/div[6]/div/div/div/div[2]/div/div/div/div[3]/button[7]',
                    findBy=By.XPATH,
                    condition=expected_conditions.element_to_be_clickable
                ).click()
                time.sleep(1.5)
                print(f"        11.{intruder_index}.2.6) Clicking \"Dangerous organizations or individuals\".")
                self.element_existence(
                    elementloc='//*[@id="igCoreRadioButtontag-3"]',
                    findBy=By.XPATH,
                    condition=expected_conditions.element_to_be_clickable
                ).click()
                time.sleep(1.5)
                print(f"        11.{intruder_index}.2.3) Clicking \"SUBMIT REPORT\"")
                self.element_existence(
                    elementloc='/html/body/div[6]/div/div/div/div[2]/div/div/div/div[6]/button',
                    findBy=By.XPATH,
                    condition=expected_conditions.element_to_be_clickable
                ).click()
                print(f"        *** @{intruder_account} has been successfully reported !")
                print("        ----------")
            except Exception:
                print("\n", "Error occurred, most likely there is no such user anymore.", "\n")
            time.sleep(3)
            self.__reported_pigs.append(intruder)

    def __cookies(self):
        self.driver.find_element(by=By.XPATH, value="/html/body/div[4]/div/div/button[1]").click()

    def __number_validation(self):
        for elem in self.driver.find_elements(by=By.TAG_NAME, value='input'):
            if elem.get_attribute("placeholder") == "Phone Number":
                print("    P.S. I don't know why this shit happened, but you need to pass the number validation.")
                print("    You have two minutes to pass this.\n")
                time.sleep(120)
                break

    def __login(self):
        username_input = self.element_existence(
            elementloc='#loginForm > div > div:nth-child(1) > div > label > input',
            findBy=By.CSS_SELECTOR,
            condition=expected_conditions.visibility_of_element_located
        )
        username_input.clear()
        username_input.send_keys(self.username)
        print("    9.1) Your USERNAME was pasted in.")
        time.sleep(1)

        password_input = self.element_existence(
            elementloc='#loginForm > div > div:nth-child(2) > div > label > input',
            findBy=By.CSS_SELECTOR,
            condition=expected_conditions.visibility_of_element_located
        )
        password_input.clear()
        password_input.send_keys(self.password)
        print("    9.2) Your PASSWORD was pasted in.")
        time.sleep(2)

        self.element_existence(
            elementloc='#loginForm > div > div:nth-child(3) > button',
            findBy=By.CSS_SELECTOR,
            condition=expected_conditions.element_to_be_clickable
        ).click()
        print("    9.3) \"LOG IN\" button was clicked.\n")

    def main(self):
        print("6. GETTING Instagram.com PAGE.\n")
        self.safe_get('https://www.instagram.com/')

        print("7. Accepting cookies.\n")
        self.__cookies()
        time.sleep(3)

        print("8. Checking if there is a number validation.\n")
        self.__number_validation()

        print("9. USER AUTHORIZATION: *If the login data are wrong, just change them.")
        self.__login()

        print("10. SLEEP FOR 10 SECONDS TO RECEIVE ALL THE DATA FROM INSTAGRAM SERVER.\n")
        time.sleep(10)

        try:
            print(f"11. STARTING REPORT OPERATION WITH {len(INTRUDERS)} INTRUDERS:")
            self.__insta_report()
            print("\n")

            print("12. CLOSING BROWSER")
            self.close_browser()

        except Exception:
            print(f"{len(self.__reported_pigs)} INTRUDERS ARE REPORTED.\n")

        print("13. STARTING OPERATIONS BY SAVING REPORTED INTRUDERS IN THE FILE:")
        self.__save_reported_pigs()
        print("..... PROGRAM FINISHED .....")
        

if __name__ == '__main__':
    print("2. INITIALIZING IstagramReport INSTANCE.\n")
    report = InstagramReport()
    print("5. RUNNING InstagramReport.main() function.\n")
    report.main()

    end = datetime.datetime.now()
    print(f"\n\n Program had been working for {end - begin}.")

    import platform
    if platform.system() == "Linux":
        os.system("pkill -f chromedriver")
