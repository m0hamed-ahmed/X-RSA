import sys
import platform,os
from urllib2 import *
from platform import system
def slowprint(s):
    for c in s :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(4. / 100)

clear = ""
if "Windows" in platform.system():
	clear = "cls"
if "Linux" in platform.system():
	clear = "clear"
os.system(clear)
is_windows = sys.platform.startswith('win')

# Console Colors
if is_windows:
    # Windows deserves coloring too :D
    G = '\033[92m'  # green
    Y = '\033[93m'  # yellow
    B = '\033[94m'  # blue
    R = '\033[91m'  # red
    W = '\033[0m'   # white
    try:
        import win_unicode_console , colorama
        win_unicode_console.enable()
        colorama.init()
        #Now the unicode will work ^_^
    except:
        print("[!] Error: Coloring libraries not installed, no coloring will be used")
        G = Y = B = R = W = G = Y = B = R = W = ''


else:
    G = '\033[92m'  # green
    Y = '\033[93m'  # yellow
    B = '\033[94m'  # blue
    R = '\033[91m'  # red
    W = '\033[0m'   # white


def banner():
    print("""%s
_____       ________________                  _____      _____
\    \     /    /\          \            _____\    \   /      |_
 \    |   |    /  \    /\    \          /    / \    | /         \\
  \    \ /    /    |   \_\    |        |    |  /___/||     /\    \\
   \    |    /     |      ___/      ____\    \ |   |||    |  |    \\
   /    |    \     |      \  ____  /    /\    \|___|/|     \/      \\
  /    /|\    \   /     /\ \/    \|    |/ \    \     |\      /\     \\
 |____|/ \|____| /_____/ |\______||\____\ /____/|    | \_____\ \_____\\
 |    |   |    | |     | | |     || |   ||    | |    | |     | |     |
 |____|   |____| |_____|/ \|_____| \|___||____|/      \|_____|\|_____|
  %s%s
[ Version : 0.2 ]\033[92m
[ Author  : X-Vector ]\033[96m
[ Github  : github.com/X-Vector ]\033[93m
[ Twitter : twitter.com/@XVector11 ]\033[95m
[ Facebook: facebook.com/X.Vector1 ]\033[95m
[ GreeteZ : Karem Ali ]\033[94m
    """ % (R, W,R))
banner()

"""
c= 3821925911648555519353747434606743159593808677487039861592438384426669998207423450606829031692403202928227703884307291926528640413305346863805555214851644456742958636273721157021584443312591620736285469414067076228984358550669307967587995994219000349054979046909041864106400708453105658165917613077273501
n= 6311257310749529896994764164885908074730315623107218148732436180339784730655096846277587690299624960654670853389184027362495475005388709090759335907428646246751073917955576737663877861242491426053238800688758573959939180213510980211538490409598005851282273664989880554327678869807688158210471903939248513
e= 65537
prime = [2160890461,2247289019,2250778319,2442210431,2458778093,2534226749,2535292559,2546035901,2651829007,2690421313,2737511971,2807722121,2985359177,3074912623,3142693039,3144852421,3159476069,3166527541,3269492927,3328687379,3493484429,3505945799,3538145749,3610828651,3699668617,3715792519,4036077043,4058968889,4089517513,4116792439,4262477123,4291039453]
"""

try:
    from fator_multi_prime import *
    import binascii
    c = int(raw_input(">>> c = "))
    n = int(raw_input(">>> n = "))
    e = int(raw_input(">>> e = "))
    slowprint("\n[+] Please Wait ...\n ")
    prime = primefactors(n)
    phi = 1
    for i in prime:
        phi *= i-1
    def egcd(a, b):
        if a == 0:
            return (b, 0, 1)
        g, y, x = egcd(b%a,a)
        return (g, x - (b//a) * y, y)
    def modinv(a, m):
        g, x, y = egcd(a, m)
        if g != 1:
            raise Exception('No modular inverse')
        return x%m
    d = modinv(e, phi)
    m = pow(c, d, n)
    def hex_pair(x):
        return ('0' * (len(x) % 2)) + x
    m_hex = '{:x}'.format(m)
    m_hex = hex_pair(m_hex)
    msg = binascii.unhexlify(m_hex)
    slowprint("\n[+] The PlainText = ")
    print(msg.decode(errors="ignore"))

except IndexError:
    slowprint("[-] Sorry Can't Factorize n ")
except ImportError:
    slowprint("\n[-] Module Not Setup")
except ValueError:
    slowprint("\n[-] c,n,e Must Be Integar Number")
except AssertionError:
    slowprint("\n[-] Wrong Data")
except Exception:
    slowprint("\n[-] Wrong Data")
except KeyboardInterrupt:
    exit()
except:
    slowprint("[-] False Attack !")
