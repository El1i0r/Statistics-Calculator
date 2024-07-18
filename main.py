#!/usr/bin/env python3

import math
import sys
from collections import Counter

def main():
    # user input, if else:
    print("...................................................................................................")
    choice = input("| Choose data type, (grouped/ungrouped) (type 1 or 2) : ")

    if choice == "2":
        while True:
            try:
                # Read input until EOF using Ctrl+D
                x = sys.stdin.read()
                xvalue = [int(num.strip()) for num in x.splitlines() if num.strip()]
                if not xvalue:
                    print("No data provided. Please enter some numbers.")
                    continue

                n = len(xvalue)
                sumx = sum(xvalue)

                # median
                xmd = float(n) + 1
                xmedian = float(xmd) / 2

                # mode
                data = Counter(xvalue)
                modes = [k for k, v in data.items() if v == max(data.values())]

                # mean
                xmean = sumx / n

                # summation of x^2
                x2sum = sum(num ** 2 for num in xvalue)

                # Variance and standard deviation
                xmean2 = xmean ** 2
                x2sumovern = x2sum / n
                variance = x2sumovern - xmean2
                std_deviation = math.sqrt(variance)

                print(f"| n = {n}")
                print(f"| Σx = {sumx}")
                print(f"| Σx² = {x2sum}")
                print(f"| Mode for this data is {modes}")
                print(f"| Median for this data is {xmedian}")
                print(f"| Mean for this data is {xmean}")
                print(f"| Variance for this data is {variance}")
                print(f"| Standard Deviation for this data is {std_deviation}")
                print("...................................................................................................")

            except ValueError:
                print("Invalid input. Please enter numbers only.")

    elif choice == "1":
        while True:
            try:
                print("× = ")
                ax = sys.stdin.read()
                axvalue = [int(num.strip()) for num in ax.splitlines() if num.strip()]
                if not axvalue:
                    print("No data provided. Please enter some numbers.")
                    continue

                print("f = ")
                f = sys.stdin.read()
                fvalue = [int(num.strip()) for num in f.splitlines() if num.strip()]
                if not fvalue:
                    print("No data provided. Please enter some numbers.")
                    continue

                #sumax = sum(axvalue)
                sumf = sum(fvalue)
                sumfx = sum(num * freq for num, freq in zip(axvalue, fvalue))
                ax2 = [num ** 2 for num in axvalue]
                sumfx2 = sum(num * freq for num, freq in zip(ax2, fvalue))

                print(f"| sumf = {sumf} and sumfx = {sumfx} and sumfx2 = {sumfx2}")

                axmean = float(sumfx) / sumf
                axmean2 = axmean ** 2
                abc = float(sumfx2) / sumf  
                avariance = abc - axmean2
                std_deviation = math.sqrt(avariance)  # Fix the typo here
                print(f"| Mean for this data is {axmean}")
                print(f"| Variance for this data is {avariance}")  # Corrected variable name
                print(f"| Standard Deviation for this data is {std_deviation}")
                print("...................................................................................................")

            except ValueError:
                print("Please enter 'human' numbers, not 'goo goo gaaa gaa' :)")

    else:
        print("Unknown choice")

if __name__ == "__main__":
    main()