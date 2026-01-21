#!/usr/bin/env python3
"""
Minecraft Launcher Tweaker
A tool to customize and enhance the Minecraft launcher
"""

import os
import sys
import json
from pathlib import Path

__version__ = "1.0.0"
__author__ = "Aayush Ranjan"

class LauncherTweaker:
    """Main class for launcher customization"""
    
    def __init__(self):
        self.config_dir = Path.home() / '.minecraft_tweaker'
        self.config_file = self.config_dir / 'config.json'
        self.setup_config()
    
    def setup_config(self):
        """Initialize configuration directory and files"""
        self.config_dir.mkdir(exist_ok=True)
        if not self.config_file.exists():
            self.save_config({
                'theme': 'dark',
                'performance': 'balanced',
                'mods_enabled': True
            })
    
    def save_config(self, config):
        """Save configuration to file"""
        with open(self.config_file, 'w') as f:
            json.dump(config, f, indent=2)
    
    def load_config(self):
        """Load configuration from file"""
        with open(self.config_file, 'r') as f:
            return json.load(f)
    
    def apply_theme(self, theme):
        """Apply UI theme"""
        print(f"Applying theme: {theme}")
    
    def optimize_performance(self, mode):
        """Optimize launcher performance"""
        print(f"Setting performance mode: {mode}")
    
    def enable_mods(self):
        """Enable mod support"""
        print("Mod support enabled")
    
    def run(self):
        """Run the launcher tweaker"""
        print(f"Minecraft Launcher Tweaker v{__version__}")
        config = self.load_config()
        self.apply_theme(config['theme'])
        self.optimize_performance(config['performance'])
        if config['mods_enabled']:
            self.enable_mods()

if __name__ == "__main__":
    tweaker = LauncherTweaker()
    tweaker.run()
