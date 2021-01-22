import re
#   envParser is able to open and read the env.txt file of the Khadas Vim
#   Classic usage would involve calling load_env_file() to get an ENV class
#   *Env file does not need to be in order

#    Use ENV.data['target'] to retrieve information about the env file.
#    Eligible ['targets'] : fan, autodetect, resolution, kernel_args,
# little_cores, big_cores

# This program prefers an env file as close to the original for all functions
# The editing autofill options functionality is only available if
# the original comments still exist

class ENV:

    def parse_cooling_fan(self, i):
        while i < len(self.lines):
            fan_mode_raw =re.search('fan_mode=(.*)', self.lines[i])
            try:return fan_mode_raw.group(1), i
            except:None
            i = i+1
        # If method makes it this far, env is out of order, cant quick search
        return self.parse_cooling_fan(i=0)

    def parse_HDMI_autodetect(self, i):
        while i < len(self.lines):
            fan_mode_raw =re.search('hdmi_autodetect=(.*)', self.lines[i])
            try:return fan_mode_raw.group(1), i
            except:None
            i = i+1
        # If method makes it this far, env is out of order, cant quick search
        return self.parse_HDMI_autodetect(i=0)

    def parse_HDMI_resolution(self, i):
        while i < len(self.lines):
            fan_mode_raw = re.search('hdmi=(.*)', self.lines[i])
            try:
                return fan_mode_raw.group(1), i
            except:
                None
            i = i + 1
        # If method makes it this far, env is out of order, cant quick search
        return self.parse_HDMI_resolution(i=0)

    def parse_user_kernel_args(self, i):
        while i < len(self.lines):
            fan_mode_raw = re.search('user_kernel_args=(.*)', self.lines[i])
            try:
                return fan_mode_raw.group(1), i
            except:
                None
            i = i + 1
        # If method makes it this far, env is out of order, cant quick search
        return self.parse_user_kernel_args(i=0)

    def parse_little_cores(self, i):
        while i < len(self.lines):
            fan_mode_raw = re.search('max_freq_a53=(.*)', self.lines[i])
            try:
                return fan_mode_raw.group(1), i
            except:
                None
            i = i + 1
        # If method makes it this far, env is out of order, cant quick search
        return self.parse_little_cores(i=0)

    def parse_big_cores(self, i):
        while i < len(self.lines):
            fan_mode_raw = re.search('max_freq_a73=(.*)', self.lines[i])
            try:
                return fan_mode_raw.group(1), i
            except:
                None
            i = i + 1
        # If method makes it this far, env is out of order, cant quick search
        return self.parse_big_cores(i=0)

    def parse_data(self):
        if self.lines is None:  # Check if self.lines is none
            print('Env not loaded from __init__')
            # self.lines was not defined in __init__
            # define self.lines manually and re-call this method
            return None
        # Otherwise parse self.line
        i=0
        self.data['fan'], i = self.parse_cooling_fan(i)
        self.data['autodetect'], i = self.parse_HDMI_autodetect(i)
        self.data['resolution'], i = self.parse_HDMI_resolution(i)
        self.data['kernel_args'], i = self.parse_user_kernel_args(i)
        self.data['little_cores'], i = self.parse_little_cores(i)
        self.data['big_cores'], i = self.parse_big_cores(i)
        #print(self.data)

    def parse_cooling_fan_options(self, i):
        start = None
        end = None
        # Find start
        while i < len(self.lines):
            fan_mode_raw =re.search('# Cooling FAN mode', self.lines[i])
            if fan_mode_raw is not None:
                start = i
                break
            i = i + 1
        # Find end
        while i < len(self.lines):
            fan_mode_raw =re.search('fan_mode=auto', self.lines[i])
            if fan_mode_raw is not None:
                end = i
                options_unparsed =self.lines[start+1:end]
                options = [re.search(r'# (.*) -',x).group(1) for x in options_unparsed]
                return options,i
            i = i + 1
        # If method makes it this far, env is out of order, cant quick search
        return self.parse_cooling_fan(i=0)

    def parse_HDMI_resoultion_options(self, i):
        start = None
        end = None
        # Find start
        while i < len(self.lines):
            raw_search =re.search('# HDMI mode', self.lines[i])
            if raw_search is not None:
                start = i
                break
            i = i + 1
        # Find end
        while i < len(self.lines):
            raw_search =re.search('hdmi=(.*)', self.lines[i])
            if raw_search is not None:
                end = i
                options_unparsed =self.lines[start+4:end]
                options = [re.search(r'"(.*)"',x).group(1) for x in options_unparsed]
                return options,i
            i = i + 1
        # If method makes it this far, env is out of order, cant quick search
        return self.parse_HDMI_resoultion_options(i=0)

    def parse_little_core_options(self, i):
        start = None
        # Find start
        while i < len(self.lines):
            raw_search =re.search('Little Core', self.lines[i])
            if raw_search is not None:
                start = i
                break
            i = i + 1
        # Find end
        while i < len(self.lines):
            raw_search =re.search('max_freq_a53', self.lines[i])
            if raw_search is not None:
                end = i
                options_unparsed =self.lines[start+1:end]
                # Clean up options
                options = [re.sub('[^0-9]', '',x) for x in options_unparsed[0].split('/')]
                return options,i
            i = i + 1
        # If method makes it this far, env is out of order, cant quick search
        return self.parse_little_core_options(i=0)

    def parse_big_core_options(self, i):
        start = None
        # Find start
        while i < len(self.lines):
            raw_search =re.search('Big Core', self.lines[i])
            if raw_search is not None:
                start = i
                break
            i = i + 1
        # Find end
        while i < len(self.lines):
            raw_search =re.search('max_freq_a73', self.lines[i])
            if raw_search is not None:
                end = i
                options_unparsed =self.lines[start+1:end]
                # Clean up options
                options = [re.sub('[^0-9]', '',x) for x in options_unparsed[0].split('/')]
                return options,i
            i = i + 1
        # If method makes it this far, env is out of order, cant quick search
        return self.parse_little_core_options(i=0)

    def parse_options(self):
        if self.lines is None:  # Check if self.lines is none
            print('Env not loaded from __init__')
            # self.lines was not defined in __init__
            # define self.lines manually and re-call this method
            return None
        # Otherwise parse self.line
        i=0
        self.options['fan'], i = self.parse_cooling_fan_options(i)
        self.options['autodetect'] = ['yes, no']  # Assuming this will never change
        self.options['resolution'], i = self.parse_HDMI_resoultion_options(i)
        # self.data['kernel_args'], i = self.parse_user_kernel_args(i)
        self.options['little_cores'], i = self.parse_little_core_options(i)
        self.options['big_cores'], i = self.parse_big_core_options(i)
        # print(self.data)

    def __init__(self, env_lines=None):  # Creating an ENV object
        self.data = {'class': self.__class__} # Will contain the env information
        self.lines = env_lines  # Add raw lines to self
        self.parse_data()  # Attempt to parse self.lines for user setting
        print(self.data)
        self.options = {'class': self.__class__}
        self.parse_options()
        print(self.options)


def load_env_file():
    env_lines = []
    with open('env.txt', 'r') as e:  # "/boot/env.txt"
        env_lines = e.readlines()
    env_lines = [e.strip().replace('\n','') for e in env_lines]
    #print(env_lines)
    environment = ENV(env_lines)
    return environment






''' env.txt file used to generate this program
#############################DO NOT TOUCH THIS OPTION#############################
rootdev=UUID=7a5f3ce3-9273-41ef-9214-06865eb1c8c9
#############################DO NOT TOUCH THIS OPTION#############################

# Cooling FAN mode
# auto -  auto schedule the FAN speed depend on the CPU temperature
# low  -  FAN low speed
# mid  -  FAN middle speed
# high -  FAN high speed
fan_mode=auto

# DMA coherent_pool size
# Don't touch unless you know what you are doing
dma_size=2M

# HDMI resolution auto detection
# yes - auto detection
# no  - set HDMI resolution via 'hdmi' node
hdmi_autodetect=yes

# HDMI mode
# Resolution Configuration
#    Symbol             | Resolution
# ----------------------+-------------
#    "480x272p60hz"     | 480x272 Progressive 60Hz
#    "480x320p60hz"     | 480x320 Progressive 60Hz
#    "480p60hz"         | 720x480 Progressive 60Hz
#    "576p50hz"         | 720x576 Progressive 50Hz
#    "720p60hz"         | 1280x720 Progressive 60Hz
#    "720p50hz"         | 1280x720 Progressive 50Hz
#    "1080p60hz"        | 1920x1080 Progressive 60Hz
#    "1080p50hz"        | 1920x1080 Progressive 50Hz
#    "1080p30hz"        | 1920x1080 Progressive 30Hz
#    "1080p24hz"        | 1920x1080 Progressive 24Hz
#    "1080i60hz"        | 1920x1080 Interlaced 60Hz
#    "1080i50hz"        | 1920x1080 Interlaced 50Hz
#    "2160p60hz"        | 3840x2160 Progressive 60Hz
#    "2160p50hz"        | 3840x2160 Progressive 50Hz
#    "2160p30hz"        | 3840x2160 Progressive 30Hz
#    "2160p25hz"        | 3840x2160 Progressive 25Hz
#    "2160p24hz"        | 3840x2160 Progressive 24Hz
#    "smpte24hz"        | 3840x2160 Progressive 24Hz SMPTE
#    "2160p60hz420"     | 3840x2160 Progressive 60Hz YCbCr 4:2:0
#    "2160p50hz420"     | 3840x2160 Progressive 50Hz YCbCr 4:2:0
#    "640x480p60hz"     | 640x480 Progressive 60Hz
#    "800x480p60hz"     | 800x480 Progressive 60Hz
#    "800x600p60hz"     | 800x600 Progressive 60Hz
#    "1024x600p60hz"    | 1024x600 Progressive 60Hz
#    "1024x768p60hz"    | 1024x768 Progressive 60Hz
#    "1280x800p60hz"    | 1280x800 Progressive 60Hz
#    "1280x1024p60hz"   | 1280x1024 Progressive 60Hz
#    "1360x768p60hz"    | 1360x768 Progressive 60Hz
#    "1440x900p60hz"    | 1440x900 Progressive 60Hz
#    "1600x900p60hz"    | 1600x900 Progressive 60Hz
#    "1600x1200p60hz"   | 1600x1200 Progressive 60Hz
#    "1680x1050p60hz"   | 1680x1050 Progressive 60Hz
#    "1920x1200p60hz"   | 1920x1200 Progressive 60Hz
#    "2560x1080p60hz"   | 2560x1080 Progressive 60Hz
#    "2560x1440p60hz"   | 2560x1440 Progressive 60Hz
#    "2560x1600p60hz"   | 2560x1600 Progressive 60Hz
#    "3440x1440p60hz"   | 3440x1440 Progressive 60Hz
hdmi=720p60hz

# Specify the initial console log level (0~8)
loglevel=7

# User kernel args
# Add customer kernel args here
user_kernel_args=

# Maximum CPU Frequency of VIM3 Little Core A53
# 500/667/1000/1200/1398/1512/1608/1704/1800(default)/1908/2016/2100/2208
max_freq_a53=2208

# Maximum CPU Frequency of VIM3 Big Core A73
# 500/667/1000/1200/1398/1512/1608/1704/1800/1908/2016/2100/2208(default)/2304/2400
max_freq_a73=2400

# Device Tree Overlays
#   uart3           -- Enable UART3 (uart_C, GPIO Header PIN15 & PIN16)
#   pwm_f           -- Enable PWM_F (GPIO Header PIN35)
#   i2c3            -- Enable i2c3 (GPIO Header PIN22 & PIN23)
#   spi1            -- Enable SPI1 (GPIO Header PIN15 & PIN16 & PIN35 & PIN37), pwm_f need to be removed
#   os08a10         -- Enable OS08A10 Camera
#   onewire         -- Enable onewire bus (GPIO Header PIN15)
#   disable-ts050   -- Disable TS050 LCD
#   m2x-eth         -- Enable M2X 100M ethernet. Note: 1G ethernet will be disabled.
overlays=uart3 pwm_f i2c3 os08a10

'''