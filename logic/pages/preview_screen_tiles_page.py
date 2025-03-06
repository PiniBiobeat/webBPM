from infra.page_base import PageBase

class PreviewScreen(PageBase):


    title_button = "//span[@style='font-weight: bold; font-size: 21px;']"
    all_selector_in_page = '//div[@class="vh_div"]'
    psifas_size = '// option[ @ value = "1"]'
    icon_add_image = "//img[@class='upload_icon']"
    icon_google = "//img[@src='/static/media/icon_google_photos.776cf4ac.svg']"
    test_logout = "//div[@class='first-row-el'][1]"
    icon_delete = "(//img[@src='/static/media/icon_trash.5d8f7be3.svg'])[1]"
    text_yes_delete = "//span[@class='lupa-btn-content' and contains(.,'כן')]"
    icon_edit = "(//img[@src='/static/media/icon_image_edit.d59295f7.svg'])[1]"
    click_to_buy = "//button[@class='lupa-btn' and contains(.,'לסל הקניות')]"
    click_to_next = "//button[@class='lupa-btn']"
    same_user = "//span[@class='lupa-btn-content' and contains(.,'כניסה')]"
    text_payment = "//button[@type='button' and contains(.,'בואו נמשיך')]"

    def __init__(self, page):
        super().__init__(page)

    def get_image(self):
        self.pw_page.wait_for_selector(self.all_selector_in_page, state="visible")
        images = self.pw_page.query_selector_all(self.all_selector_in_page)
        num_of_image = len(images)
        return num_of_image

    def get_url(self):
        # Get the current URL
        current_url = self.pw_page.url
        return current_url

    def get_price(self):
        text = self.pw_page.text_content(self.title_button)
        return text

    def button_click_to_buy(self):
        self.pw_page.click(self.click_to_next)
        self.pw_page.click(self.click_to_next)

    def button_click_to_payment(self):
        try:
            # Wait for the button to be visible and enabled
            self.pw_page.wait_for_selector("//button[@class='lupa-btn' and contains(.,'לסל הקניות')]", state="visible",
                                           timeout=5000)
            # Click the button
            self.pw_page.click("//button[@class='lupa-btn' and contains(.,'לסל הקניות')]")
        except TimeoutError as e:
            # Handle timeout errors gracefully
            print(f"TimeoutError: {e}. Button not interactable.")
            # Optionally: capture a screenshot for debugging
            self.pw_page.screenshot(path="debug_timeout.png")
        except Exception as e:
            # Handle any other errors
            print(f"Unexpected error: {e}")

    def click_with_same_user(self):
        self.pw_page.click(self.same_user)

    def click_add_image(self):
        self.pw_page.click(self.icon_add_image)

    def click_add_image_from_google(self):
        self.pw_page.click(self.icon_google)

    def click_log_out(self):
        self.pw_page.click(self.test_logout)

    def delete_image(self):
        self.pw_page.click(self.icon_delete)

    def yes_delete(self):
        self.pw_page.click(self.text_yes_delete)

    def click_edit_page(self):
        self.pw_page.click(self.icon_edit)





