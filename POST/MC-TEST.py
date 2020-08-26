import requests

url = 'https://authserver.mojang.com/authenticate'
myobj = '{"agent": {"name": "Minecraft","version": 1},"username": "connorslade@email.com","password": "YD%N#zW#JhrZkKg&pqCa9kVCcRoesyYCBJyx6GDtAN3KpZx$MK4Dc@X9zQFtmaSSveeU3HRNfy@WUw^JyS3FiQS7q*QU7b8dTEYw"}'

#url = 'https://api.mojang.com/orders/statistics'
#myobj = '{"metricKeys": ["item_sold_minecraft","prepaid_card_redeemed_minecraft"]}'

x = requests.post(url, data = myobj)

print(x.text)