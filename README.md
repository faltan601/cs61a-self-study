# 准大二 CS61A 自学

UC Berkeley CS61A（Structure and Interpretation of Computer Programs）自学记录。

## 目录

- `lectures/` — 课程代码与笔记
- `lab/` — Lab 作业
- `hw/` — Homework 作业
- `project/` — Project（Hog 等）

## 环境

- 语言：Python 
- 评测工具：`ok`（各作业目录内运行 `python ok --local`）

## 学习心得

### HW05（生成器 / generator）
- 生成器章节是前一天刚学的，第一题就卡在语法上，翻回之前上课写的代码才回忆起来，关键想起了 `yield from`。
- 第三题反而一次写出来了——一方面题目给了骨架提示，另一方面想通了一个关键点：**一直下意识以为那个函数返回的是「一条路径」，实际上它返回的是「很多条路径」，因为它是个迭代器。**

> 仅个人学习存档。课程资源版权归 UC Berkeley CS61A 所有。
