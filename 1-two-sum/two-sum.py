class Solution(object):
    def twoSum(self, nums, target):
      
         #ilk döngü dizinin her elemenını seçerMMKMK.
        for i in range(len(nums)) :  

         #ikinci döngü ,birinci döngüden sonra seçilen elemandan sonraki elamanları seçer 
            for j in range(i+1,len(nums)):

         # iki elemanın değerini hedef değerle(target) ile karşılaştırırız
                if nums[i]+ nums[j]==target:
        # eğer değer targete eşittse ,diziyi döndür
                    return[i,j]
                    

