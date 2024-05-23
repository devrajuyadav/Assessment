from appium.webdriver.common.appiumby import AppiumBy
from Pages.basepage import BasePage


class HomeSmartScreen(BasePage):
    def __init__(self, driver):
        self.driver = driver
        (super().__init__(self.driver))

    # Locators

    # Get started screen
    get_started = (AppiumBy.XPATH, "//android.widget.TextView[@text=\"Get started\"]")
    next_button = (AppiumBy.ID, "com.ikea.inter.homesmart.system2:id/primary")

    lets_get_started = (AppiumBy.XPATH,
                        "//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[2]/android.widget.Button")
    button_connect_eth_cable = (AppiumBy.XPATH,
                                "//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[2]/android.widget.Button")
    button_connect_pwr_cable = (AppiumBy.XPATH,
                                "//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[2]/android.widget.Button")
    button_wait_ring_light_circle = (AppiumBy.XPATH,
                                     "//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[3]/android.widget.Button")
    button_ring_light_pulse = (AppiumBy.XPATH,
                               "//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[3]/android.widget.Button")

    # Region screen
    region = (AppiumBy.ID, "com.ikea.inter.homesmart.system2:id/region_label")  # Sweden
    region_lets_start = (AppiumBy.ID, "com.ikea.inter.homesmart.system2:id/title")
    region_subtext = (AppiumBy.ID, "com.ikea.inter.homesmart.system2:id/message")

    # Privacy statements
    privacy_statements_title = (AppiumBy.ID, "com.ikea.inter.homesmart.system2:id/title")

    # Consent
    consent_checkbox = (AppiumBy.ID, "com.ikea.inter.homesmart.system2:id/consent_checkbox")
    no_consent_checkbox = (AppiumBy.ID, "com.ikea.inter.homesmart.system2:id/no_consent_checkbox")

    # Terms & Conditions
    tnc_hint = (AppiumBy.ID, "com.ikea.inter.homesmart.system2:id/hint")
    tnc_sharing_button = (AppiumBy.ID, "com.ikea.inter.homesmart.system2:id/secondary")
    sharing_title = (AppiumBy.XPATH, "//android.widget.TextView[@resource-id=\"android:id/text1\"]")
    button_accept = (AppiumBy.ID, "com.ikea.inter.homesmart.system2:id/primary")

    # Explore apps
    explore_apps_text = (AppiumBy.XPATH, "//android.widget.TextView[@text=\"I want to explore the app\"]")
    explore_apps_arrow = (AppiumBy.XPATH, "//android.widget.ScrollView/android.view.View[3]")

    # Dirigera hub info
    dirigera_hub = (AppiumBy.XPATH, "//android.widget.TextView[@text=\"Add a DIRIGERA hub\"]")
    why_use_dirigera_hub = (AppiumBy.XPATH, "//android.widget.TextView[@text=\"Why use a DIRIGERA hub?\"]")
    looking_for_nearby_hubs_text = (AppiumBy.XPATH, "//android.widget.TextView[@text=\"Looking for nearby hubs...\"]")

    # Expected texts
    expected_get_started = "Get started"
    expected_region = "Sweden"
    expected_region_lets_start = "Let's start with your region"
    expected_region_subtext = ('We’ll provide local Terms & Conditions so you know what to expect from the '
                               'app.')
    expected_privacy_statements_title = "Privacy Statements"
    expected_tnc_text = "Terms & Conditions"
    expected_explore_app_text = "I want to explore the app"
    expected_add_dirigera_hub_info = "Add a DIRIGERA hub"
    expected_why_use_dirigera_hub = "Why use a DIRIGERA hub?"
    expected_looking_for_nearby_hubs_text = "Looking for nearby hubs..."

    # Actions
    def scroll_end(self, n):
        for i in range(1, n):
            self.driver.swipe(300, 600, 300, 100, 100)

    def tap_get_started(self):
        self.tap_function(self.get_started)

    def tap_next(self):
        self.tap_function(self.next_button)

    def tap_consent_yes(self):
        self.tap_function(self.consent_checkbox)

    def tap_consent_no(self):
        self.tap_function(self.no_consent_checkbox)

    def tap_button_share(self):
        self.tap_function(self.tnc_sharing_button)

    def tnc_scroll_button(self):
        self.tap_function(self.tnc_hint)

    def tap_button_accept(self):
        self.tap_function(self.button_accept)

    def tap_get_started_in_home(self):
        self.tap_function(self.lets_get_started)

    def tap_button_next_1(self):
        self.tap_function(self.button_connect_eth_cable)

    def tap_button_next_2(self):
        self.tap_function(self.button_connect_pwr_cable)

    def tap_button_next_3(self):
        self.tap_function(self.button_wait_ring_light_circle)

    def tap_button_next_4(self):
        self.tap_function(self.button_ring_light_pulse)

    def tap_explore_button_arrow(self):
        self.tap_function(self.explore_apps_arrow)

    def tap_add_dirigera_hub(self):
        self.tap_function(self.dirigera_hub)

    def select_explore_app(self):
        self.tap_function(self.explore_apps_text)

    def select_explore_app_arrow(self):
        self.tap_function(self.explore_apps_arrow)

    def select_dirigera_hub(self):
        self.tap_function(self.dirigera_hub)

    def verify_get_started_screen(self):
        return self.get_text(self.get_started)

    def verify_region(self):
        return self.get_text(self.region)

    def verify_region_text(self):
        return self.get_text(self.region_lets_start)

    def verify_region_subtext(self):
        return self.get_text(self.region_subtext)

    def verify_privacy_statements_title(self):
        return self.get_text(self.privacy_statements_title)

    def verify_tnc_on_sharing_button_click(self):
        return self.get_text(self.expected_tnc_text)

    def verify_explore_apps_text(self):
        return self.get_text(self.explore_apps_text)

    def verify_add_dirigera_hub(self):
        return self.get_text(self.dirigera_hub)

    def verify_why_use_dirigera_hub(self):
        return self.get_text(self.why_use_dirigera_hub)

    def verify_looking_for_nearby_hubs(self):
        return self.get_text(self.looking_for_nearby_hubs_text)

    def verify_next_enabled(self):
        return self.enabled(self.next_button)

    def verify_accept_enabled(self):
        return self.enabled(self.button_accept)
