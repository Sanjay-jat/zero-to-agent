from langchain_community.document_loaders import WebBaseLoader
from dotenv import load_dotenv

load_dotenv()


parser=StrOutputParser()
url="https://www.flipkart.com/apple-macbook-pro-m3-8-gb-1-tb-ssd-macos-sonoma-mr7k3hn-a/p/itmcd041a34ee857?pid=COMGUTX7VWJBGPCZ&lid=LSTCOMGUTX7VWJBGPCZ1DIQ1B&marketplace=FLIPKART&q=macbook+pro+&store=6bo%2Fb5g&srno=s_1_1&otracker=search&otracker1=search&fm=organic&iid=9f8cc7db-c1b1-414c-b6b3-8fb84eb5833d.COMGUTX7VWJBGPCZ.SEARCH&ppt=None&ppn=None&ssid=qn39jzpgog0000001785509822212&qH=92a002112d0b1663&ov_redirect=true"

loader=WebBaseLoader(url)

docs=loader.load()

print(len(docs))

print(docs[0].page_content)
