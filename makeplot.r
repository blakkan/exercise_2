#
# read csv from stdin, produce a plot called plot.png
#
input.data.frame = read.csv(stdin())

count.vector = input.data.frame$Count
names(count.vector) = input.data.frame$Word

png("Plot.png")
barplot(count.vector, las=2, main = "Count of 20 most common words in tweets")
dev.off()

