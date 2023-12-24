import random

colors = {
    "purple": '\033[95m',
    "blue": '\033[94m',
    "green": '\033[92m',
    "yellow": '\033[93m',
    "red": '\033[91m',
    "endc": '\033[0m',
    "bold": '\033[1m',
    "underline": '\033[4m',
    "cyan": '\033[96m',
    "light_gray": '\033[97m',
    "dark_gray": '\033[90m',
    "white": '\033[37m',
    "orange": '\033[33m',
    "pink": '\033[95m',
    "light_blue": '\033[94m',
    "light_green": '\033[92m'
}

# colors = {
#     0: '\x1b[38;5;0m',
#     1: '\x1b[38;5;1m',
#     2: '\x1b[38;5;2m',
#     3: '\x1b[38;5;3m',
#     4: '\x1b[38;5;4m',
#     5: '\x1b[38;5;5m',
#     6: '\x1b[38;5;6m',
#     7: '\x1b[38;5;7m',
#     8: '\x1b[38;5;8m',
#     9: '\x1b[38;5;9m',
#     10: '\x1b[38;5;10m',
#     11: '\x1b[38;5;11m',
#     12: '\x1b[38;5;12m',
#     13: '\x1b[38;5;13m',
#     14: '\x1b[38;5;14m',
#     15: '\x1b[38;5;15m',
#     16: '\x1b[38;5;16m',
#     17: '\x1b[38;5;17m',
#     18: '\x1b[38;5;18m',
#     19: '\x1b[38;5;19m',
#     20: '\x1b[38;5;20m',
#     21: '\x1b[38;5;21m',
#     22: '\x1b[38;5;22m',
#     23: '\x1b[38;5;23m',
#     24: '\x1b[38;5;24m',
#     25: '\x1b[38;5;25m',
#     26: '\x1b[38;5;26m',
#     27: '\x1b[38;5;27m',
#     28: '\x1b[38;5;28m',
#     29: '\x1b[38;5;29m',
#     30: '\x1b[38;5;30m',
#     31: '\x1b[38;5;31m',
#     32: '\x1b[38;5;32m',
#     33: '\x1b[38;5;33m',
#     34: '\x1b[38;5;34m',
#     35: '\x1b[38;5;35m',
#     36: '\x1b[38;5;36m',
#     37: '\x1b[38;5;37m',
#     38: '\x1b[38;5;38m',
#     39: '\x1b[38;5;39m',
#     40: '\x1b[38;5;40m',
#     41: '\x1b[38;5;41m',
#     42: '\x1b[38;5;42m',
#     43: '\x1b[38;5;43m',
#     44: '\x1b[38;5;44m',
#     45: '\x1b[38;5;45m',
#     46: '\x1b[38;5;46m',
#     47: '\x1b[38;5;47m',
#     48: '\x1b[38;5;48m',
#     49: '\x1b[38;5;49m',
#     50: '\x1b[38;5;50m',
#     51: '\x1b[38;5;51m',
#     52: '\x1b[38;5;52m',
#     53: '\x1b[38;5;53m',
#     54: '\x1b[38;5;54m',
#     55: '\x1b[38;5;55m',
#     56: '\x1b[38;5;56m',
#     57: '\x1b[38;5;57m',
#     58: '\x1b[38;5;58m',
#     59: '\x1b[38;5;59m',
#     60: '\x1b[38;5;60m',
#     61: '\x1b[38;5;61m',
#     62: '\x1b[38;5;62m',
#     63: '\x1b[38;5;63m',
#     64: '\x1b[38;5;64m',
#     65: '\x1b[38;5;65m',
#     66: '\x1b[38;5;66m',
#     67: '\x1b[38;5;67m',
#     68: '\x1b[38;5;68m',
#     69: '\x1b[38;5;69m',
#     70: '\x1b[38;5;70m',
#     71: '\x1b[38;5;71m',
#     72: '\x1b[38;5;72m',
#     73: '\x1b[38;5;73m',
#     74: '\x1b[38;5;74m',
#     75: '\x1b[38;5;75m',
#     76: '\x1b[38;5;76m',
#     77: '\x1b[38;5;77m',
#     78: '\x1b[38;5;78m',
#     79: '\x1b[38;5;79m',
#     80: '\x1b[38;5;80m',
#     81: '\x1b[38;5;81m',
#     82: '\x1b[38;5;82m',
#     83: '\x1b[38;5;83m',
#     84: '\x1b[38;5;84m',
#     85: '\x1b[38;5;85m',
#     86: '\x1b[38;5;86m',
#     87: '\x1b[38;5;87m',
#     88: '\x1b[38;5;88m',
#     89: '\x1b[38;5;89m',
#     90: '\x1b[38;5;90m',
#     91: '\x1b[38;5;91m',
#     92: '\x1b[38;5;92m',
#     93: '\x1b[38;5;93m',
#     94: '\x1b[38;5;94m',
#     95: '\x1b[38;5;95m',
#     96: '\x1b[38;5;96m',
#     97: '\x1b[38;5;97m',
#     98: '\x1b[38;5;98m',
#     99: '\x1b[38;5;99m',
#     100: '\x1b[38;5;100m',
#     101: '\x1b[38;5;101m',
#     102: '\x1b[38;5;102m',
#     103: '\x1b[38;5;103m',
#     104: '\x1b[38;5;104m',
#     105: '\x1b[38;5;105m',
#     106: '\x1b[38;5;106m',
#     107: '\x1b[38;5;107m',
#     108: '\x1b[38;5;108m',
#     109: '\x1b[38;5;109m',
#     110: '\x1b[38;5;110m',
#     111: '\x1b[38;5;111m',
#     112: '\x1b[38;5;112m',
#     113: '\x1b[38;5;113m',
#     114: '\x1b[38;5;114m',
#     115: '\x1b[38;5;115m',
#     116: '\x1b[38;5;116m',
#     117: '\x1b[38;5;117m',
#     118: '\x1b[38;5;118m',
#     119: '\x1b[38;5;119m',
#     120: '\x1b[38;5;120m',
#     121: '\x1b[38;5;121m',
#     122: '\x1b[38;5;122m',
#     123: '\x1b[38;5;123m',
#     124: '\x1b[38;5;124m',
#     125: '\x1b[38;5;125m',
#     126: '\x1b[38;5;126m',
#     127: '\x1b[38;5;127m',
#     128: '\x1b[38;5;128m',
#     129: '\x1b[38;5;129m',
#     130: '\x1b[38;5;130m',
#     131: '\x1b[38;5;131m',
#     132: '\x1b[38;5;132m',
#     133: '\x1b[38;5;133m',
#     134: '\x1b[38;5;134m',
#     135: '\x1b[38;5;135m',
#     136: '\x1b[38;5;136m',
#     137: '\x1b[38;5;137m',
#     138: '\x1b[38;5;138m',
#     139: '\x1b[38;5;139m',
#     140: '\x1b[38;5;140m',
#     141: '\x1b[38;5;141m',
#     142: '\x1b[38;5;142m',
#     143: '\x1b[38;5;143m',
#     144: '\x1b[38;5;144m',
#     145: '\x1b[38;5;145m',
#     146: '\x1b[38;5;146m',
#     147: '\x1b[38;5;147m',
#     148: '\x1b[38;5;148m',
#     149: '\x1b[38;5;149m',
#     150: '\x1b[38;5;150m',
#     151: '\x1b[38;5;151m',
#     152: '\x1b[38;5;152m',
#     153: '\x1b[38;5;153m',
#     154: '\x1b[38;5;154m',
#     155: '\x1b[38;5;155m',
#     156: '\x1b[38;5;156m',
#     157: '\x1b[38;5;157m',
#     158: '\x1b[38;5;158m',
#     159: '\x1b[38;5;159m',
#     160: '\x1b[38;5;160m',
#     161: '\x1b[38;5;161m',
#     162: '\x1b[38;5;162m',
#     163: '\x1b[38;5;163m',
#     164: '\x1b[38;5;164m',
#     165: '\x1b[38;5;165m',
#     166: '\x1b[38;5;166m',
#     167: '\x1b[38;5;167m',
#     168: '\x1b[38;5;168m',
#     169: '\x1b[38;5;169m',
#     170: '\x1b[38;5;170m',
#     171: '\x1b[38;5;171m',
#     172: '\x1b[38;5;172m',
#     173: '\x1b[38;5;173m',
#     174: '\x1b[38;5;174m',
#     175: '\x1b[38;5;175m',
#     176: '\x1b[38;5;176m',
#     177: '\x1b[38;5;177m',
#     178: '\x1b[38;5;178m',
#     179: '\x1b[38;5;179m',
#     180: '\x1b[38;5;180m',
#     181: '\x1b[38;5;181m',
#     182: '\x1b[38;5;182m',
#     183: '\x1b[38;5;183m',
#     184: '\x1b[38;5;184m',
#     185: '\x1b[38;5;185m',
#     186: '\x1b[38;5;186m',
#     187: '\x1b[38;5;187m',
#     188: '\x1b[38;5;188m',
#     189: '\x1b[38;5;189m',
#     190: '\x1b[38;5;190m',
#     191: '\x1b[38;5;191m',
#     192: '\x1b[38;5;192m',
#     193: '\x1b[38;5;193m',
#     194: '\x1b[38;5;194m',
#     195: '\x1b[38;5;195m',
#     196: '\x1b[38;5;196m',
#     197: '\x1b[38;5;197m',
#     198: '\x1b[38;5;198m',
#     199: '\x1b[38;5;199m',
#     200: '\x1b[38;5;200m',
#     201: '\x1b[38;5;201m',
#     202: '\x1b[38;5;202m',
#     203: '\x1b[38;5;203m',
#     204: '\x1b[38;5;204m',
#     205: '\x1b[38;5;205m',
#     206: '\x1b[38;5;206m',
#     207: '\x1b[38;5;207m',
#     208: '\x1b[38;5;208m',
#     209: '\x1b[38;5;209m',
#     210: '\x1b[38;5;210m',
#     211: '\x1b[38;5;211m',
#     212: '\x1b[38;5;212m',
#     213: '\x1b[38;5;213m',
#     214: '\x1b[38;5;214m',
#     215: '\x1b[38;5;215m',
#     216: '\x1b[38;5;216m',
#     217: '\x1b[38;5;217m',
#     218: '\x1b[38;5;218m',
#     219: '\x1b[38;5;219m',
#     220: '\x1b[38;5;220m',
#     221: '\x1b[38;5;221m',
#     222: '\x1b[38;5;222m',
#     223: '\x1b[38;5;223m',
#     224: '\x1b[38;5;224m',
#     225: '\x1b[38;5;225m',
#     226: '\x1b[38;5;226m',
#     227: '\x1b[38;5;227m',
#     228: '\x1b[38;5;228m',
#     229: '\x1b[38;5;229m',
#     230: '\x1b[38;5;230m',
#     231: '\x1b[38;5;231m',
#     232: '\x1b[38;5;232m',
#     233: '\x1b[38;5;233m',
#     234: '\x1b[38;5;234m',
#     235: '\x1b[38;5;235m',
#     236: '\x1b[38;5;236m',
#     237: '\x1b[38;5;237m',
#     238: '\x1b[38;5;238m',
#     239: '\x1b[38;5;239m',
#     240: '\x1b[38;5;240m',
#     241: '\x1b[38;5;241m',
#     242: '\x1b[38;5;242m',
#     243: '\x1b[38;5;243m',
#     244: '\x1b[38;5;244m',
#     245: '\x1b[38;5;245m',
#     246: '\x1b[38;5;246m',
#     247: '\x1b[38;5;247m',
#     248: '\x1b[38;5;248m',
#     249: '\x1b[38;5;249m',
#     250: '\x1b[38;5;250m',
#     251: '\x1b[38;5;251m',
#     252: '\x1b[38;5;252m',
#     253: '\x1b[38;5;253m',
#     254: '\x1b[38;5;254m',
#     255: '\x1b[38;5;255m'
# }

def colored(text:str, color:str) -> str:
    return f"{colors[color]}{text}\033[0m"


def rand_colored(text:str) -> str:
    return f"{colored(text, random.choice(colors))}"