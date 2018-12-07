import xlwt        
from collections import Counter        
 
book = xlwt.Workbook() # create a new excel file
sheet_test = book.add_sheet('word_count') # add a new sheet
i = 0
sheet_test.write(i,0,'word') # write the header of the first column
sheet_test.write(i,1,'count') # write the header of the second column

with open('C:\\Python34\\text_word1.txt','r') as text_word1: # read the txtfile containing the words
   count_result =Counter(text_word1.read().split())
   for result in count_result.most_common(10):
        i = i+1 
        sheet_test.write(i,0,result[0])
        sheet_test.write(i,1,result[1])      
    
book.save('C:\\Python34\\word_count1.xls')# save your result in an execel file
