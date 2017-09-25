import webbrowser
import argparse

parser = argparse.ArgumentParser(description="顯示在參數說明前的訊息",epilog="顯示在參數說明後的訊息")
parser.add_argument("-u","--url",type=str,help="輸入網址",default = "http://www.ntou.edu.tw")

args = parser.parse_args()

if __name__ == "__main__":
#	if not args.url.startswith("http"):
#		args.url = "http://" + args.url
	webbrowser.open(args.url)
