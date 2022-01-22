#
#
# Copyright (c) 2022 Samiun Nafis (samiunnafis.github.io). All rights reserved.
#
# License under the GNU General Public License, Version 3.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.gnu.org/licenses/gpl-3.0.en.html
#
# Unless required by the applicable law or agreed in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from time import sleep
import pyautogui as auto
import schedule, webbrowser

# Gmeet Code
code = "kvy-qhny-kjb"

# Time of class 24hours
time = "19:12" 


def join():
    webbrowser.open_new_tab('https://meet.google.com/' + code)
    sleep(7)
    # for windows and linux
    auto.hotkey('ctrl', 'd')
    auto.hotkey('ctrl', 'e')
    # for macOS
    #auto.hotkey('command', 'd')
    #auto.hotkey('command', 'e')
    auto.click(1034, 569)


schedule.every().day.at(time).do(join)

while True:
    schedule.run_pending()
    sleep(1)