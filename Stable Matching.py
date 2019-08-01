# -*- encoding: UTF-8 -*-

'''
伪代码：

# 首先初始化所有男生的状态为自由
initialize each person to be free

# 当男生没有未曾被匹配过并且也没有向所有其他女生寻求舞伴过时不断循环
while some man m is not yet matched:
    # 每个男生按照对女生的喜欢程度选择舞伴
    w := m's most favroite woman to whom he has not yet proposed
    # 如果女生未被匹配到，则与男生进行配对
    if w is also not yet matched:
        w and m are paired
    # 如果女生与已匹配的男生相比更喜欢当前的这个男生，则拆散重新匹配
    elif w favors m to her current matched m':
        w and m are paired and m' is dis-matched
    # 否则该女生拒绝成为男生的舞伴
    else:
        w rejects m
# 返回所有匹配成功的舞伴对
return matched pairs


'''














import copy

# 男的所期望的对象
manPrefers = dict((m, prefs.split(', ')) for [m, prefs] in (line.rstrip().split(': ')
                                                            for line in open('men.txt')))
# 女的所期望的对象
womenPrefers = dict((m, prefs.split(', ')) for [m, prefs] in (line.rstrip().split(': ')
                                                              for line in open('women.txt')))

men = sorted(manPrefers.keys())
women = sorted(womenPrefers.keys())


# 定义检测函数检测匹配的伴侣是否稳定
def check(engaged):
    inverseengaged = dict((v, k) for k, v in engaged.items())
    for w, m in engaged.items():
        shelikes = womenPrefers[w]
        shelikesbetter = shelikes[:shelikes.index(m)]
        helikes = manPrefers[m]
        helikesbetter = helikes[:helikes.index(w)]
        for man in shelikesbetter:
            womenOftheMan = inverseengaged[man]
            manLoves = manPrefers[man]
            if manLoves.index(womenOftheMan) > manLoves.index(w):
                print("%s 和 %s 更喜欢彼此相比起他们当前的伴侣: %s 和 %s" % (w, man, m, womenOftheMan))
                return False
        for woman in helikesbetter:
            manOfTheWomen = engaged[woman]
            womanLoves = womenPrefers[woman]
            if womanLoves.index(manOfTheWomen) > womanLoves.index(m):
                print("%s 和 %s 更喜欢彼此相比起他们当前的伙伴：%s 和 %s" % (m, woman, w, manOfTheWomen))
                return False
    return True


def stableMatching():
    free_men = men[:]
    engaged = {}
    manPref_temp = copy.deepcopy(manPrefers)
    womenPref_temp = copy.deepcopy(womenPrefers)
    while free_men:
        man = free_men.pop(0)
        manList = manPref_temp[man]
        woman = manList.pop(0)
        fiance = engaged.get(woman)
        if not fiance:
            engaged[woman] = man
            print("  %s 和 %s 成为伴侣" % (man, woman))
        else:
            womenList = womenPref_temp[woman]
            if womenList.index(fiance) > womenList.index(man):
                engaged[woman] = man
                print("  %s 舍弃 %s 而和 %s 成为伴侣" % (woman, fiance, man))
                if manPref_temp[fiance]:
                    free_men.append(fiance)
            else:
                if manList:
                    free_men.append(man)
    return engaged


if __name__ == '__main__':
    print('\n伴侣匹配:')
    engaged = stableMatching()

    print('\n伴侣匹配:')
    print('  ' + ',\n  '.join('%s 和 %s 成为伴侣' % couple for couple in sorted(engaged.items())))
    print()
    print('伴侣稳定性检测通过' if check(engaged) else '伴侣稳定性检测不通过')

    print('\n\n因交换而产生伴侣搭配错误')
    engaged[women[0]], engaged[women[1]] = engaged[women[1]], engaged[women[0]]
    for woman in women[:2]:
        print('  %s 现在和 %s 成为伴侣' % (woman, engaged[woman]))
    print()
    print('伴侣稳定性检测通过' if check(engaged) else '伴侣稳定性检测不通过')
