#Awards - Portfolio
#Certificates - Portfolio
#Projects - BLOG
#VIA/SIP - Portfolio
#Personal statement - About domnic

class portfolioItem:
    #portfolioItemType: Award/Certificate/VIA~SIP
    #portfolioItemList
    #portfolioItemImageURL
    def __init__(self, portfolioItemClassList, portfolioItemName, portfolioItemList, portfolioItemImageURL, portfolioItemGithubLink = None):
        self.portfolioItemGithubLink = portfolioItemGithubLink
        self.portfolioItemClassList = portfolioItemClassList
        self.portfolioItemName = portfolioItemName
        self.portfolioItemList = portfolioItemList
        self.portfolioItemImageURL = portfolioItemImageURL
    def __repr__(self):
        return f"{self.portfolioItemItem}, {self.portfolioItemName}, {self.portfolioItemList}, {self.portfolioItemImageURL}"

class portfolio:
    def __init__(self):
        self.portfolioItems = list()
        with open('data/portfolio.txt', 'r') as portfolio:
            lines = portfolio.readlines()
            currentPortfolioItemLines = list()
            for line in lines:
                currentPortfolioItemLines.append(line)
                if line == "\n":
                    #portfolioItemClassList
                    portfolioItemClassList = currentPortfolioItemLines[0].replace("\n", "")
                    portfolioItemClassList = portfolioItemClassList.split(" ")
                    tempDict = {
                        "Award" : "gal_a",
                        "Certificate" : "gal_b",
                        "VIA/SIP" : "gal_c",
                        "Project" : "gal_d"
                    }
                    for idx, portfolioItemClassListItem in enumerate(portfolioItemClassList):
                        portfolioItemClassList[idx] = tempDict[portfolioItemClassListItem]
                    if "gal_d" in portfolioItemClassList:
                        portfolioItemName = currentPortfolioItemLines[1]
                        portfolioItemList = list()
                        for i in range(2, len(currentPortfolioItemLines) - 2):
                            portfolioItemList.append(currentPortfolioItemLines[i])
                        portfolioItemImageURL = f'static\\images\\{portfolioItemName.replace(" ", "-").replace("|", "").replace("/", "")}.png'
                        portfolioItemGithubLink = currentPortfolioItemLines[-2]
                        currentPortfolioItem = portfolioItem(portfolioItemClassList=portfolioItemClassList, portfolioItemName=portfolioItemName, portfolioItemList=portfolioItemList, portfolioItemImageURL=portfolioItemImageURL, portfolioItemGithubLink=portfolioItemGithubLink)
                        self.portfolioItems.append(currentPortfolioItem)
                        currentPortfolioItemLines.clear()
                    else:

                        #portfolioItemName
                        portfolioItemName = currentPortfolioItemLines[1]
                        #portfolioItemList
                        portfolioItemList = list()
                        for i in range(2, len(currentPortfolioItemLines) - 1):
                            portfolioItemList.append(currentPortfolioItemLines[i])
                        #portfolioItemImageURL
                        portfolioItemImageURL = f'static\\images\\{portfolioItemName.replace(" ", "-").replace("|", "")}.png'
                        currentPortfolioItem = portfolioItem(portfolioItemClassList=portfolioItemClassList, portfolioItemName=portfolioItemName, portfolioItemList=portfolioItemList, portfolioItemImageURL=portfolioItemImageURL)
                        self.portfolioItems.append(currentPortfolioItem)
                        currentPortfolioItemLines.clear()
    def output(self):
        for portfolioItem in self.portfolioItems:
            print(portfolioItem)

