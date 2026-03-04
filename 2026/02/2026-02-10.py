

def time_to_sec(tstring):
    timeSplit = str(tstring).split(":")
    timeSec = ((int(timeSplit[0]) * 60) * 60) + (int(timeSplit[1]) * 60) + int(timeSplit[2])
    return timeSec


def get_relative_results(results):
    sortedTimes = sorted(results)
    secArray = [time_to_sec(i) for i in sortedTimes]
    winner = secArray[0]
    diffArray = [f"+{int((i - winner)/60)}:{(i - winner) % 60:02d}" for i in secArray]
    diffArray[0] = "0"

    print(diffArray)

    
    return diffArray

assert get_relative_results(["1:25:32", "1:26:10", "1:27:05"]) == ["0", "+0:38", "+1:33"]
assert get_relative_results(["1:00:01", "1:00:05", "1:00:10"]) == ["0", "+0:04", "+0:09"]
assert get_relative_results(["1:10:06", "1:10:23", "1:10:48", "1:12:11"]) == ["0", "+0:17", "+0:42", "+2:05"]
assert get_relative_results(["0:49:13", "0:49:15", "0:50:14", "0:51:30", "0:51:58", "0:52:16", "0:53:12", "0:53:31", "0:56:19", "1:02:20"]) == ["0", "+0:02", "+1:01", "+2:17", "+2:45", "+3:03", "+3:59", "+4:18", "+7:06", "+13:07"]
assert get_relative_results(["2:01:15", "2:10:45", "2:10:53", "2:11:04", "2:11:55", "2:13:27", "2:14:30", "2:15:10"]) == ["0", "+9:30", "+9:38", "+9:49", "+10:40", "+12:12", "+13:15", "+13:55"]