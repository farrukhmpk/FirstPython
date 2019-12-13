#
#    Copyright 2018 Farrukh Mirza
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#

# To run, type $python HwlloWorld.py
#https://www.learnpython.org/
input = {10 ,5 ,20, 15}

input = sorted(input)

for worldCount in input:
    # x = 20
    print("Hello World %d!" %worldCount)

    if worldCount > 10:
        print("Too many Worlds")
    elif worldCount < 10:
        print("Where is everyone")
    else:
        print("Ahhh! Perfect!")
