import json
from collections import Counter

def is_anagram(str1, str2):
    # Remove spaces and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # If lengths are different, they cannot be anagrams
    if len(str1) != len(str2):
        return False
    
    # Use Counter to count character frequencies
    freq1 = Counter(str1)
    freq2 = Counter(str2)
    
    # Check if both Counters are equal
    return freq1 == freq2

def lambda_handler(event, context):
    # Get input strings from event
    str1 = event['str1']
    str2 = event['str2']
    
    # Check if strings are anagrams
    result = is_anagram(str1, str2)
    
    # Return result
    return {
        'statusCode': 200,
        'body': json.dumps({
            'isAnagram': result
        })
    }
