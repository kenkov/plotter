#! /usr/bin/env python
# coding:utf-8

import sys
from collections import namedtuple
import matplotlib
import matplotlib.pyplot as plt


Point = namedtuple("Point", ["x", "ys"])


class Parser:
    """一行からプロットする数値情報を抜き出すクラス"""
    def __init__(self, separator):
        self.separator = separator

    def parse(self, line):
        """一行をパースして数値情報を抜き出す。

        Args:
            line (str): プロット数値情報が入った一行
        Returns:
            Point: プロットする Point
        """
        items = line.strip("\n").split(self.separator)
        x = float(items[0])
        ys = tuple(float(y) for y in items[1:])
        return Point(x=x, ys=ys)


class Plotter:
    """Point をプロットするクラス。"""
    def __init__(self, savefig, legend, loc, title, xlabel, ylabel):
        self.savefig = savefig
        self.legend = legend
        self.loc = loc
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel

    def plot(self, points):
        """Point をプロットする。

        Args:
            points (List[Point]): 描画する点 Point のリスト
        """
        xs = [pt.x for pt in points]
        vals = list(zip(*[pt.ys for pt in points]))
        styles = ["-o", "--o", "-.o", ":o"]

        for i, ys in enumerate(vals):
            plt.plot(xs, ys, styles[i % len(styles)])
        if self.legend:
            plt.legend(self.legend, loc=self.loc)
        if self.title:
            plt.title(self.title)
        if self.xlabel:
            plt.xlabel(self.xlabel)
        if self.ylabel:
            plt.ylabel(self.ylabel)

        if self.savefig:
            plt.savefig(self.savefig)
        else:
            print(f"show figure with {matplotlib.get_backend()} backend",
                  file=sys.stderr)
            plt.show()


def plot(args):
    parser = Parser(separator=args.separator)
    plotter = Plotter(savefig=args.savefig,
                      legend=args.legend,
                      loc=args.loc,
                      title=args.title,
                      xlabel=args.xlabel,
                      ylabel=args.ylabel)
    points = []
    for line in sys.stdin:
        points.append(parser.parse(line))

    plotter.plot(points)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--savefig',
                        type=str,
                        help=('save figure as filename.',
                              'if not specified, try to plot with backend'))
    parser.add_argument('--separator',
                        type=str,
                        default=" ",
                        help='separator')
    parser.add_argument('--legend',
                        action="append",
                        help='legend for each data')
    parser.add_argument('--loc',
                        default="upper right",
                        help='location of legend')
    parser.add_argument('--title',
                        help='title')
    parser.add_argument('--xlabel',
                        help='name of axis of x')
    parser.add_argument('--ylabel',
                        help='name of axis of y')
    args = parser.parse_args()
    plot(args)
