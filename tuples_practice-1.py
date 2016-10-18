
n = '1','2','3','4','5'



tup = 'hi', 'bye'


first = 'Joe'


print first[0]



print first[-3:]


var1 = tuple("hey")
var2 = tuple("you")

var1, var2 = var2, var1
print var1
print var2


date = 'Jan 15 2016'

month, day, year = ('Jan', '15', '2016')
print month
print day
print year


t = divmod(18, 9)

print t


t4 = (7,5)
divmod(*t4)
print t4



print zip('Joe', 'Vandoorn')




Months = [('Feb',1),('Mar',1),('Apr',1),('May',1),('June',1),('July',1),]



month_dict = dict(Months)
print month_dict



def sort_by_length(words):
    t = []
    for word in words:
        t.append((len(word), word))

    t.sort(reverse=True)
    res = []
    for length, word in t:
        res.append(word)
    return res



my_words = ['Cat', 'Dog', 'Mouse', 'Lion', 'Snake']

print sort_by_length(my_words)
