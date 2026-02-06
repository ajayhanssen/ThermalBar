import numpy as np

def main():
    x = np.linspace(0,100,100)

    print(x.T@x)
    


if __name__ == "__main__":
    main()
