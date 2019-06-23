# Write a program that prints the numbers 1 to 100, however:
#
# 1) If the number is a multiple of 3 print "Fizz" instead of the number.
# 2) If the number is a multiple of 5 print "Buzz" instead of the number.
# 3) For the numbers which are multiples of both 3 and 5 print "FizzBuzz"
# instead of the number.
#
# Remember, break the problem up in to manageable chunks. Upon reading, you should
# see “Write a program that prints the numbers 1 to 100” and stop, because
# you already have enough information to write code and make that happen.
# Delete that part of the question from your attention span and continue reading
# until you reach another point where you have enough information to write code.
# Continue this process until you’ve solved the entire problem. You can do it!
#
# Note: There is no instant feedback for this question other than verification
# that your code doesn’t raise errors.
(1..100).each{|num|p num%15==0?"FizzBuzz":num%5==0?"Buzz":num%3==0?"Fizz":num}
# def fizzbuzz?(num)
#   case
#   when num % 15 == 0 then "FizzBuzz"
#   when num % 3  == 0 then "Fizz"
#   when num % 5  == 0 then "Buzz"
#   else num
#   end
# end
