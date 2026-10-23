import contextlib
import io
import runpy
import unittest
from pathlib import Path

with contextlib.redirect_stdout(io.StringIO()):
    ns = runpy.run_path(str(Path(__file__).with_name("entertainment_system.py")))


class TestEntertainmentSystem(unittest.TestCase):
    def setUp(self):
        self.tv, self.dvd = ns["Television"](), ns["DVDPlayer"]()
        self.console, self.router = ns["GameConsole"](), ns["Router"]()

    def test_connections(self):
        self.assertEqual(self.tv.connect_to_dvd("dvd"), f"connected {self.tv} to dvd via RCI connection")
        self.assertEqual(self.dvd.connect_to_tv("tv"), f"connected {self.dvd} to tv via HDMI connection")
        self.assertEqual(self.console.connect_to_router("r"), f"connected {self.console} to r via Ethernet connection")
        self.assertEqual(self.router.connect_to_game_console("c"),
                         f"connected {self.router} to c via Ethernet connection")

    def test_only_needed_interfaces(self):
        self.assertFalse(hasattr(self.dvd, "connect_to_device_via_ethernet_cable"))
        self.assertFalse(hasattr(self.router, "connect_to_device_via_hdmi_cable"))

    def test_plug_in_power(self):
        self.assertEqual(self.router.plug_in_power(), f"connected {self.router} to power supply")


if __name__ == "__main__":
    unittest.main()
