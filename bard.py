import bard
from bardapi import BardCookies
import datetime

cookie_dict ={
    "__Secure-1PSID" : "bQhuVisizX6gmibLTAyPNMPbm7CdwC9mKI7NY2BCyCFg2G6HN1vMtA7KxVoMPgYAc0Z44w.",
    "__Secure-1PSIDTS" : "sidts-CjEB3e41hX2gWJM-9d_mEN3ScJ1pTo1avzieIsmulZX4mf8EA_nxrWMbNCj1TpJ_gjjbEAA",
    "__Secure-1PSIDCC" : "sidts-CjEB3e41hX2gWJM-9d_mEN3ScJ1pTo1avzieIsmulZX4mf8EA_nxrWMbNCj1TpJ_gjjbEAA"
    }

bard = BardCookies(cookie_dict=cookie_dict)

while True:
        Query = input("Enter The Query : ")
        Reply = bard.get_answer(Query)['content']
        print(Reply)