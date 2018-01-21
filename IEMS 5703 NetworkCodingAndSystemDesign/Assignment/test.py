def problem_05(sentence):
    output = []
    counts = dict()
    words = sentence.lower().split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    L = []
    for key, value in counts.items():
        L.append((value, key))
    output = sorted(L, key=lambda x: x[0], reverse=True)
    output = output[0:5]
    return output


sentence = """
   The Transmission Control Protocol (TCP) is one of the main protocols of the Internet protocol suite. It originated in the initial network implementation in which it complemented the Internet Protocol (IP). Therefore, the entire suite is commonly referred to as TCP/IP. TCP provides reliable, ordered, and error-checked delivery of a stream of octets between applications running on hosts communicating by an IP network. Major Internet applications such as the World Wide Web, email, remote administration, and file transfer rely on TCP. Applications that do not require reliable data stream service may use the User Datagram Protocol (UDP), which provides a connectionless datagram service that emphasizes reduced latency over reliability.
"""
print(problem_05(sentence))