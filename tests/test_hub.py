import time
import pytest

@pytest.mark.usefixtures("android", "ikea_hub")
class TestHubTesting:
    @pytest.mark.first
    def test_initial_screen(self, android, ikea_hub):
        assert ikea_hub.verify_get_started_screen() == ikea_hub.expected_get_started
        ikea_hub.tap_get_started()
        time.sleep(2)

    @pytest.mark.second
    def test_start_region(self, android, ikea_hub):
        assert ikea_hub.verify_region() == ikea_hub.expected_region
        assert ikea_hub.verify_region_text() == ikea_hub.expected_region_lets_start
        assert ikea_hub.verify_region_subtext() == ikea_hub.expected_region_subtext
        ikea_hub.tap_next()

    @pytest.mark.third
    def test_privacy_statements(self, android, ikea_hub):
        assert ikea_hub.verify_privacy_statements_title() == ikea_hub.expected_privacy_statements_title
        assert not ikea_hub.verify_next_enabled(), ("Next button should not be enabled "
                                                    "until user goes through complete privacy statements")
        ikea_hub.scroll_end(3)
        assert ikea_hub.verify_next_enabled(), "Privacy : Next button should be enabled"
        ikea_hub.tap_next()
        time.sleep(1)

    @pytest.mark.fourth
    def test_consent_analytics(self, android, ikea_hub):
        assert not ikea_hub.verify_next_enabled(), ("Next button should not be enabled "
                                                    "until the user has accepted/declined the consent")
        ikea_hub.tap_consent_no()
        assert ikea_hub.verify_next_enabled(), "Consent : Next button should be enabled"
        ikea_hub.scroll_end(2)
        ikea_hub.tap_consent_yes()
        ikea_hub.tap_next()
        time.sleep(2)

    @pytest.mark.fifth
    def test_terms_conditions(self, android, ikea_hub):
        assert not ikea_hub.verify_accept_enabled(), ("Terms and conditions : Accept button should not"
                                                      "be enabled until user has gone through the T&C")
        # there is an arrow button, which when clicked will take to the last and buttons will be enabled
        ikea_hub.scroll_end(6)
        assert ikea_hub.verify_accept_enabled(), "T&C : Accept button should be enabled"

        # click button accept
        ikea_hub.tap_button_accept()

    @pytest.mark.sixth
    def test_explore_app(self, android, ikea_hub):
        ikea_hub.scroll_end(3)
        assert ikea_hub.verify_explore_apps_text() == ikea_hub.expected_explore_app_text
        # Query : only the arrow is clickable here !! any specific reason
        ikea_hub.tap_explore_button_arrow()

    @pytest.mark.seventh
    def test_home_screen(self, android, ikea_hub):
        assert ikea_hub.verify_add_dirigera_hub() == ikea_hub.expected_add_dirigera_hub_info
        # clicking on add dirigera hub opens a screen
        ikea_hub.tap_add_dirigera_hub()
        # text : Why use a DIRIGERA hub?
        assert ikea_hub.verify_why_use_dirigera_hub() == ikea_hub.expected_why_use_dirigera_hub
        ikea_hub.tap_add_dirigera_hub()
        ikea_hub.tap_add_dirigera_hub()
        # click Started followed by Next
        ikea_hub.tap_get_started()
        ikea_hub.tap_button_next_1()
        ikea_hub.tap_button_next_2()
        ikea_hub.tap_button_next_3()
        ikea_hub.tap_button_next_4()

        assert ikea_hub.verify_looking_for_nearby_hubs() == ikea_hub.expected_looking_for_nearby_hubs_text

