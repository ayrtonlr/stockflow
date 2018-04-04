# StockFlow

Final project of Code:Nation course.

A web application using Django that allows you to create multiple portfolios and organizing their stocks in your own way. The values of the most diverse stocks are presented in a clear and detailed way. It is possible to display a graph with the latest values of the stock, the latest news from the company and also if it is a good moment to buy or sell your stock.

The **instructions file** can be used to help you run the application in your PC.

### Homepage

Homepage's view where the users can log in, register or reset the password.

![Stockflow Homepage](/images/homepage.png)

### Wallet

Wallet's view where the users can create their own wallets with the companies that they want to follow.

![Wallet](/images/wallet.png)

### Wallet Info

Info Wallet's view where the users can see what the companies that they are following.

![Wallet Info](/images/wallet_info.png)

### Company

Company's view where the users can see everything from that specific company. The page uses Scrapy to get news, description, website and informations about the company. A graph is shown with the last values of the company's stock and with using a little bit of data science, the page advises it it is a good moment to buy or sell your stock. 

![Company](/images/company.png)
