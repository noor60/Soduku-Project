#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 11:11:52 2020

@author: nooreen
"""
import sys
sys.setrecursionlimit(111500)

def show(board):
    for i in range(len(board)):
        if i % 3 == 0:
            if i == 0:
                print(" ┎────────┰────────┰────────┒")
            else:
                print(" ┠────────╂────────╂────────┨")

        for j in range(len(board[0])):
            if j % 3 == 0:
                print(" ┃", end=" ")

            if j == 8:
                print(board[i][j], " ┃")
            else:
                print(board[i][j], end=" ")

    print(" ┖────────┸────────┸────────┚")


board = [[3, 7, 0, 5, 0, 0, 0, 0, 6],
         [0, 0, 0, 3, 6, 0, 0, 1, 2],
         [0, 0, 0, 0, 9, 1, 7, 5, 0],
         [0, 0, 0, 1, 5, 4, 0, 7, 0],
         [0, 0, 3, 0, 7, 0, 6, 0, 0],
         [0, 5, 0, 6, 3, 8, 0, 0, 0],
         [0, 6, 4, 9, 8, 0, 0, 0, 0],
         [5, 9, 0, 0, 2, 6, 0, 0, 0],
         [2, 0, 0, 0, 0, 5, 0, 6, 4]]

def exists_in_row(board,number, empty_i):
    for i in range(len(board[0])):
        if board[empty_i][i] == number:
            return False

def exists_in_column(board,number, empty_j):
    for i in range(len(board[0])):
        if board[i][empty_j] == number:
            return False


def check_in_column(number):
    for i in range(len(board[0])):
        return False


def check_in_box(number):
    for i in range(len(board[0])):
        return False


def valid_options_for_current_cell(board, number,current_empty_row,current_empty_column):
    
    # Check row
    for i in range(len(board[0])):
        if board[current_empty_row][i] == number and current_empty_column != i:
            return False
    # Check column
    for i in range(len(board)):
        if board[i][current_empty_column] == number and current_empty_row != i:
            return False
    # Check box
    box_x = current_empty_column // 3
    box_y = current_empty_row // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if board[i][j] == number and (i, j) != current_empty_column and current_empty_row:
                return False

    return True

def boxposition(element):
    board_pos = 0
    if element == 0 or element <= 2:
        board_pos = 0
    if element > 2 and element < 6:
        board_pos = 3
    if element > 5 and element < 9:
        board_pos = 6
    return (board_pos)


def backtrack(current_empty_row, current_empty_column):
    board[current_empty_row][current_empty_column - 1] = 0


def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                return i, j


def solve(board):
    empty_slots = find_empty(board)
    if not empty_slots:
        return True
    else:
        current_empty_row, current_empty_column = empty_slots


    for number in range(1, 10):
        if valid_options_for_current_cell(board, number, current_empty_row, current_empty_column):
            board[current_empty_row][current_empty_column] = number

            if solve(board):
                return True

            board[current_empty_row][current_empty_column]=0
    return False


show(board);
solve(board);
print(" Sodoku puzzle at initial state")
print("________________________________")

show(board);

print(" Sodoku puzzle at final stage")
print("________________________________")


