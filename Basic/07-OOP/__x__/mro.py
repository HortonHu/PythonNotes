# -*- coding:utf-8 -*-


# __mro__
# 返回一个类的MRO的tuple
# 只有新式类才可以调用 采用C3算法 merge操作就是C3算法的核心。


# 如果继承至一个基类A:
# class B(A)
# 这时B的mro(B)为(<class 'A'>, <type 'object'>)


# 如果继承至多个基类
# class B(A1,A2,A3 ...)
# 这时B的mro序列 mro(B) = [B] + merge(mro(A1), mro(A2), mro(A3) ..., [A1,A2,A3...])
# 遍历执行merge操作的序列，如果一个序列的第一个元素，是其他序列中的第一个元素，
# 或不在其他序列出现，则从所有执行merge操作序列中删除这个元素，合并到当前的mro中。
# merge操作后的序列，继续执行merge操作，直到merge操作的序列为空。
# 如果merge操作的序列无法为空，则说明不合法。
# 例如：
# class A(O):pass
# class B(O):pass
# class C(O):pass
# class E(A,B):pass
# class F(B,C):pass
# class G(E,F):pass
# A、B、C都继承至一个基类，所以mro序列依次为[A,O]、[B,O]、[C,O]
# mro(E) = [E] + merge(mro(A), mro(B), [A,B])
#        = [E] + merge([A,O], [B,O], [A,B])
#        = [E,A,B] + merge([O], [O])
#        = [E,A,B,O]
# mro(F) = [F,B,C,O]
# mro(G) = [G] + merge(mro[E], mro[F], [E,F])
#        = [G] + merge([E,A,B,O], [F,B,C,O], [E,F])
#        = [G,E] + merge([A,B,O], [F,B,C,O], [F])
#        = [G,E,A] + merge([B,O], [F,B,C,O], [F])
#        = [G, E, A, F] + merge([B, O], [B, C, O])
#        = [G, E, A, F, B] + merge([O], [C, O])
#        = [G, E, A, F, B, C] + merge([O], [O])
#        = [G, E, A, F, B, C, O]


