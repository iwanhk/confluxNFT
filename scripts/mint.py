from scripts.functions import *


def main():
    active_network = network.show_active()
    print("Current Network:" + active_network)

    admin, creator, consumer, iwan = get_accounts(active_network)

    try:
        if active_network in LOCAL_NETWORKS:
            nft=NFT.deploy(10000, 3125, 3, "http://isotop.top/", addr(admin))
            nft.setupNonAuctionSaleInfo(0, chain.time())
            # nft.mint(100, addr2(creator, 0))
            # for i in range(100):
            #     nft.transferFrom(creator, nft, i, addr(creator))


        if active_network in TEST_NETWORKS:
            nft=NFT[-1]
            nft.sale(creator, 4, addr(admin))
            nft.fit(addr(creator))
            nft.fit(addr(creator))
            

    except Exception:
        console.print_exception()
        # Test net contract address


if __name__ == "__main__":
    main()
