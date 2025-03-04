class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def is_dividing(big_str, sml_str) -> bool:
            big_len, sml_len = len(big_str), len(sml_str)
            if big_len % sml_len != 0:
                return False

            for i in range(big_len // sml_len):
                if big_str[i*sml_len: (i+1)*sml_len] != sml_str:
                    return False
            return True

        big_len, sml_len = len(str1), len(str2)
        if big_len < sml_len:
            big_len, sml_len = sml_len, big_len
            big_str, sml_str = str2, str1
        else:
            big_str, sml_str = str1, str2

        answer = ''
        for i in range(1, sml_len+1):
            candidate = sml_str[0:i]
            # print(f'Trying candidate: {candidate}')
            if is_dividing(sml_str, candidate) and is_dividing(big_str, candidate):
                answer = candidate
                # print(f'Updated answer to: {answer}')

        return answer


        


        

