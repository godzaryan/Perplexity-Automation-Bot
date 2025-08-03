from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.common.exceptions import TimeoutException
import time
import traceback

FIREFOX_PROFILE_PATH = r"C:\Users\crono\AppData\Roaming\Mozilla\Firefox\Profiles\7ouab8p1.default-release"
FIREFOX_BINARY_PATH = r"C:\Program Files\Mozilla Firefox\firefox.exe"

PROMPT_INPUT_XPATH = (
    "//div[@contenteditable='true' and @role='textbox' and "
    "(contains(@aria-placeholder, 'Ask anything') or contains(@aria-placeholder, 'Ask a follow-up'))]"
)
RESPONSE_CONTAINERS_XPATH = "//div[starts-with(@id, 'markdown-content-')]"
STOP_BUTTON_CSS = 'button[data-testid="stop-generating-response-button"]'

WAIT_PAGE_LOAD = 30
CHAR_DELAY = 0.05
GENERATION_TIMEOUT = 120

def wait_for_generation_complete(driver, timeout=GENERATION_TIMEOUT):
    wait = WebDriverWait(driver, timeout)
    try:
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, STOP_BUTTON_CSS)))
    except TimeoutException:
        pass
    try:
        wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, STOP_BUTTON_CSS)))
    except TimeoutException:
        pass

def send_prompt(driver, prompt_text):
    wait = WebDriverWait(driver, WAIT_PAGE_LOAD)
    input_div = wait.until(EC.visibility_of_element_located((By.XPATH, PROMPT_INPUT_XPATH)))

    actions = ActionChains(driver)
    actions.move_to_element(input_div).click().perform()
    time.sleep(0.3)

    actions = ActionChains(driver)
    actions.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).send_keys(Keys.BACKSPACE).perform()
    time.sleep(0.3)

    for ch in prompt_text:
        actions.send_keys(ch)
        actions.pause(CHAR_DELAY)
    actions.send_keys(Keys.RETURN)
    actions.perform()

def get_latest_response(driver):
    wait_for_generation_complete(driver)

    wait = WebDriverWait(driver, WAIT_PAGE_LOAD)
    response_containers = wait.until(
        EC.presence_of_all_elements_located((By.XPATH, RESPONSE_CONTAINERS_XPATH))
    )
    if response_containers:
        last_response = response_containers[-1]
        return last_response.text.strip()
    return "[WARNING] No response found."

def main():
    print("Starting Perplexity AI automation with your Firefox profile.")
    profile = FirefoxProfile(FIREFOX_PROFILE_PATH)
    options = Options()
    options.profile = profile
    options.binary_location = FIREFOX_BINARY_PATH

    driver = webdriver.Firefox(options=options)

    try:
        print("Loading https://www.perplexity.ai/ ...")
        driver.get("https://www.perplexity.ai/")
        WebDriverWait(driver, WAIT_PAGE_LOAD).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )
        WebDriverWait(driver, WAIT_PAGE_LOAD).until(
            EC.visibility_of_element_located((By.XPATH, PROMPT_INPUT_XPATH))
        )

        while True:
            user_prompt = input("\nEnter prompt (or 'exit' or empty to quit): ").strip()
            if user_prompt.lower() == "exit" or not user_prompt:
                print("Exiting automation.")
                break

            print(f"\nSending prompt:\n{user_prompt}")
            send_prompt(driver, user_prompt)

            print("Waiting for Perplexity to finish...")
            response = get_latest_response(driver)
            print("\n--- Perplexity AI Response ---\n")
            print(response)
            print("\n-----------------------------")

    except Exception:
        print("An error occurred:")
        print(traceback.format_exc())

    finally:
        driver.quit()
        print("Browser closed.")

if __name__ == "__main__":
    main()
