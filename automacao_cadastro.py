import pandas as pd
import robot

if __name__ == "__main__":
    df = pd.read_excel('cadastro_clientes.xlsx')
    robot.cadastro_web(df)