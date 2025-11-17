DESCRIBE ALL TABLES;
SELECT G.gnomeName, SUM(GP.quantity) AS 'TOTAL GNOMES SOLD'
FROM Gnome G
JOIN GnomePurchase GP ON GP.gnomeID = G.gnomeID
WHERE g.description LIKE '%solar%' 
GROUP BY G.gnomeName
ORDER BY sum(GP.quantity) DESC;