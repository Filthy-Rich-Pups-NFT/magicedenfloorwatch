import time
import requests


def floorcheck(symbol):
    '''check nft floor on magiceden'''
    base_url = "http://api-mainnet.magiceden.dev/v2/collections/"
    api_url = base_url + symbol + "/stats"
    response = requests.get(api_url)
    result = response.json()
    floorprice = int(result['floorPrice'])/1000000000
    
    return floorprice


def listings_collections_latest(symbol,limit=20):
    '''IMPORTANT: max limit for endpoint is 20'''
    base_url = "http://api-mainnet.magiceden.dev/v2/collections/"
    suffix = "/listings?offset=0&limit="
    limit = str(limit)
    api_url = base_url + symbol + suffix + limit    
    response = requests.get(api_url)
    result = response.json() 

    return result



def code(symbol_list):
    for symbol in symbol_list:
        floor = float(floorcheck(symbol))
        listings = listings_collections_latest(symbol)
        for result in listings:
            tokenMint = result["tokenMint"]
            tokenPrice = result["price"]
            print("Token Mint: " + str(tokenMint) + ". Token Price: " + str(tokenPrice) + ". Floor Price: " + str(floor))
        
        time.sleep(2)


def main():
    symbol_list = ["degods","okay_bears","great__goats","galactic_geckos","cets_on_creck"]
    while True:
        try:
            code(symbol_list)
        except KeyboardInterrupt:
            print("You pressed ctrl c...")
            break
        except Exception as e:
            print(e)
            
if __name__ == "__main__":

    main()




