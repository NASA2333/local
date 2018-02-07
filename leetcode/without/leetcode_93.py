'''
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)


'''

def restoreIpAddresses(s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []
        _restoreIpAddresses(0, s, [], result)
        return result

def _restoreIpAddresses(length, s, ips, result):
    if not s:
        if length == 4:
            result.append('.'.join(ips))
        return
    elif length == 4:
        return
    _restoreIpAddresses(length + 1, s[1:], ips + [s[:1]], result)
    if s[0] != '0':
        if len(s) >= 2:
            _restoreIpAddresses(length + 1, s[2:], ips + [s[:2]], result)
        if len(s) >= 3 and int(s[:3]) <= 255:
            _restoreIpAddresses(length + 1, s[3:], ips + [s[:3]], result)
print(restoreIpAddresses('25525511135'))