def core_i9():
    while True:
        print("\n--- Intel Core I9 Gen 11 ---")
        user_choice = int(input(
            "1. Specification\n2. BenchMark\n3. Note\n4. Summary\n5. Back to Main Page\n Enter the things you want(1/2/3/4/5): "))
        if user_choice == 1:
            print("\nThis is the specification of intel core i9")
            print("Number of Cores: 8.\nTotal Threads: 16.\nCPU Clock Speed: Up to 5.20GHz.\nCache Size: 24MB.\nMemory Support Up to DDR5 4800MT.\nIntegrated Graphics Intel Iris Xe.\n")
        elif user_choice == 2:
            print("Not Available\n")
        elif user_choice == 3:
            print("\nNote:")
            print("The benchmark scores of the listed processors are averages measured across various devices with these processors. The scores and real-world performance of the Intel Core i9 gen 11 and compared CPUs may vary depending on the notebooks' other components, settings, cooling, and other factors. However, the benchmark results are good indicators of the processors performance.\n")
        elif user_choice == 4:
            print("\nSummary:")
            print("Overall, The Intel Core i9 is a high-end processor that is considered one of the best available PC components on the market. It offers a high level of performance and is well-suited for tasks that require a lot of processing power, such as video editing, 3D rendering, and gaming.\n")
        elif user_choice == 5:
            main()


def core_i5():
    while True:
        print("\n--- Intel Core I5 Gen 11 ---")
        user_choice = int(input(
            "1. Specification\n2. BenchMark\n3. Note\n4. Summary\n5. Back to Main Page\n Enter the things you want(1/2/3/4/5): "))
        if user_choice == 1:
            print("\nThis is the specification of intel core i5")
            print("Number of Cores: Quad-core / 2 computing threads per core.\nCPU Clock Speed: Up to 4.2 GHz.\nCache Size: 8MB.\nMemory Support DDR4 (3200 MHz max. speed) LPDDR4 (4266 MHz max. speed).\nIntegrated Graphics Intel Iris Xe\n.")
        elif user_choice == 2:
            print("Not Available\n")
        elif user_choice == 3:
            print("\nNote:")
            print("The benchmark scores of the listed processors are averages measured across various devices with these processors. The scores and real-world performance of the Intel Core i5 gen 11 and compared CPUs may vary depending on the notebooks' other components, settings, cooling, and other factors. However, the benchmark results are good indicators of the processors performance.\n")
        elif user_choice == 4:
            print("\nSummary:")
            print("\nOverall, all three chips can flawlessly handle the daily home and office computing tasks, but the i5 and i7 variants provide extra oomph for heavier duties like video editing. These two are also better in terms of 3D gaming performance. They feature the Intel Iris Xe graphics, which is faster than the Intel UHD G4 of the Core i3. However, all of these graphics processors are in the entry-level category when it comes to gaming.\n")
        elif user_choice == 5:
            main()


def ryzen7():
    while True:
        print("\n--- Intel Core I5 Gen 11 ---")
        user_choice = int(input(
            "1. Specification\n2. BenchMark\n3. Note\n4. Summary\n5. Back to Main Page\n Enter the things you want(1/2/3/4/5): "))
        if user_choice == 1:
            print("\nThis is the specification of ryzen7")
            print("CPU cores: 8.\nThread: 16.\nClock Speed: Up to 4.7GHz.\nMemory support: DDR5, LPDDR5.\nCache size: 20mb.\n")
        elif user_choice == 2:
            print("Not Available\n")
        elif user_choice == 3:
            print("\nNote:")
            print("The benchmark scores of the listed processors are averages measured across various devices with these processors. The scores and real-world performance of the Intel Core i5 gen 11 and compared CPUs may vary depending on the notebooks' other components, settings, cooling, and other factors. However, the benchmark results are good indicators of the processors performance.\n")
        elif user_choice == 4:
            print("\nSummary:")
            print("\nThis is relatively new CPU that contains 8 Cores and 16 Threads. The AMD Ryzen 7 6800H also has reasonable threaded performance that will serve well in games. Paired with a good videocard, is this CPU Good for Gaming? Yes, this would be a suitable CPU for gaming.")
        elif user_choice == 5:
            main()


def main():
    while True:
        print("\n--- Main Page ---")
        user_choice = int(input(
            "1. Intel core i9\n2. Intel core i5\n3. Ryzen 7\n4. quit\nEnter the product you want to know about(1/2/3/4): "))
        if user_choice == 1:
            core_i9()
        elif user_choice == 2:
            core_i5()
        elif user_choice == 3:
            ryzen7()
        else:
              break


main()
