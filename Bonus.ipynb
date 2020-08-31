{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 106,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import sqlalchemy\n",
    "import pprint\n",
    "import psycopg2\n",
    "import matplotlib.pyplot as plt\n",
    "%matplotlib inline"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 107,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sqlalchemy import create_engine\n",
    "#engine = create_engine('postgresql://localhost:5432/sql-homework')\n",
    "db_url = (f\"postgresql+psycopg2://postgres:Ahadu2014@localhost:5432/sql-homework\")\n",
    "engine = create_engine(db_url)\n",
    "connection = engine.connect()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 117,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>emp_no</th>\n",
       "      <th>salary</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>10001</td>\n",
       "      <td>60117</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>10002</td>\n",
       "      <td>65828</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>10003</td>\n",
       "      <td>40006</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>10004</td>\n",
       "      <td>40054</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>10005</td>\n",
       "      <td>78228</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   emp_no  salary\n",
       "0   10001   60117\n",
       "1   10002   65828\n",
       "2   10003   40006\n",
       "3   10004   40054\n",
       "4   10005   78228"
      ]
     },
     "execution_count": 117,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "salaries = pd.read_sql(\"SELECT * FROM salaries\", connection)\n",
    "salaries.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 122,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>emp_no</th>\n",
       "      <th>title_id</th>\n",
       "      <th>birth_date</th>\n",
       "      <th>first_name</th>\n",
       "      <th>last_name</th>\n",
       "      <th>sex</th>\n",
       "      <th>hire_date</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>473302</td>\n",
       "      <td>s0001</td>\n",
       "      <td>1953-07-25</td>\n",
       "      <td>Hideyuki</td>\n",
       "      <td>Zallocco</td>\n",
       "      <td>M</td>\n",
       "      <td>1990-04-28</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>475053</td>\n",
       "      <td>e0002</td>\n",
       "      <td>1954-11-18</td>\n",
       "      <td>Byong</td>\n",
       "      <td>Delgrande</td>\n",
       "      <td>F</td>\n",
       "      <td>1991-09-07</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>57444</td>\n",
       "      <td>e0002</td>\n",
       "      <td>1958-01-30</td>\n",
       "      <td>Berry</td>\n",
       "      <td>Babb</td>\n",
       "      <td>F</td>\n",
       "      <td>1992-03-21</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>421786</td>\n",
       "      <td>s0001</td>\n",
       "      <td>1957-09-28</td>\n",
       "      <td>Xiong</td>\n",
       "      <td>Verhoeff</td>\n",
       "      <td>M</td>\n",
       "      <td>1987-11-26</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>282238</td>\n",
       "      <td>e0003</td>\n",
       "      <td>1952-10-28</td>\n",
       "      <td>Abdelkader</td>\n",
       "      <td>Baumann</td>\n",
       "      <td>F</td>\n",
       "      <td>1991-01-18</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   emp_no title_id  birth_date  first_name  last_name sex   hire_date\n",
       "0  473302    s0001  1953-07-25    Hideyuki   Zallocco   M  1990-04-28\n",
       "1  475053    e0002  1954-11-18       Byong  Delgrande   F  1991-09-07\n",
       "2   57444    e0002  1958-01-30       Berry       Babb   F  1992-03-21\n",
       "3  421786    s0001  1957-09-28       Xiong   Verhoeff   M  1987-11-26\n",
       "4  282238    e0003  1952-10-28  Abdelkader    Baumann   F  1991-01-18"
      ]
     },
     "execution_count": 122,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "employees = pd.read_sql(\"SELECT * FROM employees\", connection)\n",
    "employees.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 119,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>title_id</th>\n",
       "      <th>title</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>s0001</td>\n",
       "      <td>Staff</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>s0002</td>\n",
       "      <td>Senior Staff</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>e0001</td>\n",
       "      <td>Assistant Engineer</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>e0002</td>\n",
       "      <td>Engineer</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>e0003</td>\n",
       "      <td>Senior Engineer</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  title_id               title\n",
       "0    s0001               Staff\n",
       "1    s0002        Senior Staff\n",
       "2    e0001  Assistant Engineer\n",
       "3    e0002            Engineer\n",
       "4    e0003     Senior Engineer"
      ]
     },
     "execution_count": 119,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "titles = pd.read_sql(\"SELECT * FROM titles\", connection)\n",
    "titles.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 123,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>emp_no</th>\n",
       "      <th>salary</th>\n",
       "      <th>title_id</th>\n",
       "      <th>birth_date</th>\n",
       "      <th>first_name</th>\n",
       "      <th>last_name</th>\n",
       "      <th>sex</th>\n",
       "      <th>hire_date</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>10001</td>\n",
       "      <td>60117</td>\n",
       "      <td>e0003</td>\n",
       "      <td>1953-09-02</td>\n",
       "      <td>Georgi</td>\n",
       "      <td>Facello</td>\n",
       "      <td>M</td>\n",
       "      <td>1986-06-26</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>10002</td>\n",
       "      <td>65828</td>\n",
       "      <td>s0001</td>\n",
       "      <td>1964-06-02</td>\n",
       "      <td>Bezalel</td>\n",
       "      <td>Simmel</td>\n",
       "      <td>F</td>\n",
       "      <td>1985-11-21</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>10003</td>\n",
       "      <td>40006</td>\n",
       "      <td>e0003</td>\n",
       "      <td>1959-12-03</td>\n",
       "      <td>Parto</td>\n",
       "      <td>Bamford</td>\n",
       "      <td>M</td>\n",
       "      <td>1986-08-28</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>10004</td>\n",
       "      <td>40054</td>\n",
       "      <td>e0003</td>\n",
       "      <td>1954-05-01</td>\n",
       "      <td>Chirstian</td>\n",
       "      <td>Koblick</td>\n",
       "      <td>M</td>\n",
       "      <td>1986-12-01</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>10005</td>\n",
       "      <td>78228</td>\n",
       "      <td>s0001</td>\n",
       "      <td>1955-01-21</td>\n",
       "      <td>Kyoichi</td>\n",
       "      <td>Maliniak</td>\n",
       "      <td>M</td>\n",
       "      <td>1989-09-12</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   emp_no  salary title_id  birth_date first_name last_name sex   hire_date\n",
       "0   10001   60117    e0003  1953-09-02     Georgi   Facello   M  1986-06-26\n",
       "1   10002   65828    s0001  1964-06-02    Bezalel    Simmel   F  1985-11-21\n",
       "2   10003   40006    e0003  1959-12-03      Parto   Bamford   M  1986-08-28\n",
       "3   10004   40054    e0003  1954-05-01  Chirstian   Koblick   M  1986-12-01\n",
       "4   10005   78228    s0001  1955-01-21    Kyoichi  Maliniak   M  1989-09-12"
      ]
     },
     "execution_count": 123,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Create a merged dataframe of employees and salary\n",
    "combined_data = pd.merge(salaries, employees, on=\"emp_no\", how=\"inner\")\n",
    "combined_data.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 124,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>title_id</th>\n",
       "      <th>title</th>\n",
       "      <th>emp_no</th>\n",
       "      <th>salary</th>\n",
       "      <th>birth_date</th>\n",
       "      <th>first_name</th>\n",
       "      <th>last_name</th>\n",
       "      <th>sex</th>\n",
       "      <th>hire_date</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>s0001</td>\n",
       "      <td>Staff</td>\n",
       "      <td>10002</td>\n",
       "      <td>65828</td>\n",
       "      <td>1964-06-02</td>\n",
       "      <td>Bezalel</td>\n",
       "      <td>Simmel</td>\n",
       "      <td>F</td>\n",
       "      <td>1985-11-21</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>s0001</td>\n",
       "      <td>Staff</td>\n",
       "      <td>10005</td>\n",
       "      <td>78228</td>\n",
       "      <td>1955-01-21</td>\n",
       "      <td>Kyoichi</td>\n",
       "      <td>Maliniak</td>\n",
       "      <td>M</td>\n",
       "      <td>1989-09-12</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>s0001</td>\n",
       "      <td>Staff</td>\n",
       "      <td>10007</td>\n",
       "      <td>56724</td>\n",
       "      <td>1957-05-23</td>\n",
       "      <td>Tzvetan</td>\n",
       "      <td>Zielinski</td>\n",
       "      <td>F</td>\n",
       "      <td>1989-02-10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>s0001</td>\n",
       "      <td>Staff</td>\n",
       "      <td>10011</td>\n",
       "      <td>42365</td>\n",
       "      <td>1953-11-07</td>\n",
       "      <td>Mary</td>\n",
       "      <td>Sluis</td>\n",
       "      <td>F</td>\n",
       "      <td>1990-01-22</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>s0001</td>\n",
       "      <td>Staff</td>\n",
       "      <td>10016</td>\n",
       "      <td>70889</td>\n",
       "      <td>1961-05-02</td>\n",
       "      <td>Kazuhito</td>\n",
       "      <td>Cappelletti</td>\n",
       "      <td>M</td>\n",
       "      <td>1995-01-27</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  title_id  title  emp_no  salary  birth_date first_name    last_name sex  \\\n",
       "0    s0001  Staff   10002   65828  1964-06-02    Bezalel       Simmel   F   \n",
       "1    s0001  Staff   10005   78228  1955-01-21    Kyoichi     Maliniak   M   \n",
       "2    s0001  Staff   10007   56724  1957-05-23    Tzvetan    Zielinski   F   \n",
       "3    s0001  Staff   10011   42365  1953-11-07       Mary        Sluis   F   \n",
       "4    s0001  Staff   10016   70889  1961-05-02   Kazuhito  Cappelletti   M   \n",
       "\n",
       "    hire_date  \n",
       "0  1985-11-21  \n",
       "1  1989-09-12  \n",
       "2  1989-02-10  \n",
       "3  1990-01-22  \n",
       "4  1995-01-27  "
      ]
     },
     "execution_count": 124,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "combined_data2 = pd.merge(titles, combined_data, on=\"title_id\", how=\"inner\")\n",
    "combined_data2.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 125,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>emp_no</th>\n",
       "      <th>salary</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>title</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Assistant Engineer</th>\n",
       "      <td>252992.595373</td>\n",
       "      <td>48564.434447</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Engineer</th>\n",
       "      <td>253654.345919</td>\n",
       "      <td>48535.336511</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Manager</th>\n",
       "      <td>110780.833333</td>\n",
       "      <td>51531.041667</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Senior Engineer</th>\n",
       "      <td>253038.749885</td>\n",
       "      <td>48506.799871</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Senior Staff</th>\n",
       "      <td>254481.798969</td>\n",
       "      <td>58550.172704</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Staff</th>\n",
       "      <td>253408.503604</td>\n",
       "      <td>58465.382850</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Technique Leader</th>\n",
       "      <td>251811.432730</td>\n",
       "      <td>48582.896092</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                           emp_no        salary\n",
       "title                                          \n",
       "Assistant Engineer  252992.595373  48564.434447\n",
       "Engineer            253654.345919  48535.336511\n",
       "Manager             110780.833333  51531.041667\n",
       "Senior Engineer     253038.749885  48506.799871\n",
       "Senior Staff        254481.798969  58550.172704\n",
       "Staff               253408.503604  58465.382850\n",
       "Technique Leader    251811.432730  48582.896092"
      ]
     },
     "execution_count": 125,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "grouped_df = combined_data2.groupby(\"title\").mean()\n",
    "grouped_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 126,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[<matplotlib.axes._subplots.AxesSubplot object at 0x00000153E01A8C88>]],\n",
       "      dtype=object)"
      ]
     },
     "execution_count": 126,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAXQAAAEICAYAAABPgw/pAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4xLjMsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+AADFEAAAXAklEQVR4nO3dfZAcdZ3H8feHJESOhaBGVy7kXCyid0jKh4yAhVfOgneEhwKrDq14qMSH2hLFp4I6glShUnUnqEhpYcnFgxJ8YEHQuhzBUk5d0ToBd7mQJQZ00fVIgjwYDAwCVuR7f0ynGCYzO729vZnd33xeVVPb0/379fy+05NPenqmpxURmJnZ/LdftwdgZmblcKCbmSXCgW5mlggHuplZIhzoZmaJcKCbmSXCgW4GSApJR3R7HGYz4UA3M0uEA91sBiQt7PYYzPZwoFtyJJ0vabukJyTdJ+kESUdL+rmkP0p6UNIVkvZv0/8USf8r6XFJD0j6VMOygezwzPsk/R/wI0kbJX24aR2bJb11dis1ez4HuiVF0quAc4A3RMRBwInAJPAX4OPAUuCNwAnAB9us5kng3cAhwCnA2S3C+c3A32XrvwZ4Z8MYXgMsA24ppSiznBzolpq/AIuBIyUtiojJiLg/IsYi4vaI2B0Rk8C/Uw/lvUTESESMR8SzEbEZuK5F209FxJMR8RTwn8AKSSuyZe8Cro+IP89GgWbtONAtKRExAXwM+BTwsKRhSX8t6ZWSbpb0e0mPA/9GfW99L5KOkfRjSY9I2gV8oEXbBxoe8xngBuCdkvYD3gF8vfTizDpwoFtyIuJbEfEm4OVAAJcCXwHuBVZExMHAJwC1WcW3gA3A8ohYAlzZom3zz5ReA5xJ/VDOnyLi52XUYjYdDnRLiqRXSTpe0mLgaeAp6odhDgIeB2qS/hY4e4rVHATsjIinJR0N/HOnx80C/FngMrx3bl3iQLfULAYuAR4Ffg+8lPre+HnUg/kJ4KvA9VOs44PAxZKeAC6ifjglj2uBlcA3Co3cbIbkC1yYlUPSu4Gh7HCP2T7nPXSzEkj6K+p79uu7PRbrXQ50sxmSdCLwCPAQ9Q9UzbrCh1zMzBLhPXQzs0R07YeFli5dGgMDA916+K548sknOfDAA7s9jH2m1+qF3qu51+qF7tc8Njb2aES8pNWyrgX6wMAAo6Oj3Xr4rhgZGaFarXZ7GPtMr9ULvVdzr9UL3a9Z0u/aLfMhFzOzRDjQzcwS4UA3M0uEA93MLBEOdDOzRDjQzcwSkTvQJS3IrrN4c4tliyVdL2lC0h2SBsocpJmZdTadPfSPAlvbLHsf8FhEHAFcTv2CAmZmtg/lCnRJh1G/WO5/tGlyOvUrtgDcCJwgqd3VYMzMbBbk+nEuSTcCn6F+JZfzIuLUpuX3AKsjYlt2/37gmIh4tKndEDAE0N/fv2p4eLjQoMe37yrUrwwrly0p3LdWq9HX11fiaOa2XqsXeq/mXqsXul/z4ODgWERUWi3reOq/pFOBhyNiTFK1XbMW8/b6nyIi1pP9XnSlUomip8+uXbexUL8yTJ5ZLdy326cM72u9Vi/0Xs29Vi/M7ZrzHHI5DjhN0iQwDBwvqfkSW9uA5QCSFgJLgJ0ljtPMzDroGOgRcUFEHBYRA8Aa4EcR8c6mZhuAs7LpM7I2/qF1M7N9qPCvLUq6GBiNiA3AVcDXJU1Q3zNfU9L4zMwsp2kFekSMACPZ9EUN858G3lbmwMzMbHp8pqiZWSIc6GZmiXCgm5klwoFuZpYIB7qZWSIc6GZmiXCgm5klwoFuZpYIB7qZWSIc6GZmiXCgm5klwoFuZpYIB7qZWSIc6GZmiXCgm5klwoFuZpaIjoEu6QWS7pR0t6Qtkj7dos1aSY9I2pTd3j87wzUzs3byXLHoGeD4iKhJWgT8TNL3IuL2pnbXR8Q55Q/RzMzy6Bjo2cWea9ndRdnNF4A2M5tjch1Dl7RA0ibgYeDWiLijRbN/krRZ0o2Slpc6SjMz60j1HfCcjaVDgO8CH46IexrmvxioRcQzkj4AvD0ijm/RfwgYAujv7181PDxcaNDj23cV6leGlcuWFO5bq9Xo6+srcTRzW6/VC71Xc6/VC92veXBwcCwiKq2WTSvQASR9EngyIj7fZvkCYGdETJl8lUolRkdHp/XYewys21ioXxkmLzmlcN+RkRGq1Wp5g5njeq1e6L2ae61e6H7NktoGep5vubwk2zNH0gHAW4B7m9oc2nD3NGBr8eGamVkReb7lcihwTbbnvR9wQ0TcLOliYDQiNgAfkXQasBvYCaydrQGbmVlreb7lshl4XYv5FzVMXwBcUO7QzMxsOnymqJlZIhzoZmaJcKCbmSXCgW5mlggHuplZIhzoZmaJcKCbmSXCgW5mlggHuplZIhzoZmaJcKCbmSXCgW5mlggHuplZIhzoZmaJcKCbmSXCgW5mlggHuplZIvJcU/QFku6UdLekLZI+3aLNYknXS5qQdIekgdkYrJmZtZdnD/0Z4PiIeA3wWmC1pGOb2rwPeCwijgAuBy4td5hmZtZJx0CPulp2d1F2i6ZmpwPXZNM3AidIUmmjNDOzjhTRnM0tGkkLgDHgCODLEXF+0/J7gNURsS27fz9wTEQ82tRuCBgC6O/vXzU8PFxo0OPbdxXqV4aVy5YU7lur1ejr6ytxNHNbr9ULvVdzr9UL3a95cHBwLCIqrZYtzLOCiPgL8FpJhwDflXRURNzT0KTV3vhe/1NExHpgPUClUolqtZrn4feydt3GQv3KMHlmtXDfkZERitY8H/VavdB7NfdavTC3a57Wt1wi4o/ACLC6adE2YDmApIXAEmBnCeMzM7Oc8nzL5SXZnjmSDgDeAtzb1GwDcFY2fQbwo8hzLMfMzEqT55DLocA12XH0/YAbIuJmSRcDoxGxAbgK+LqkCep75mtmbcRmZtZSx0CPiM3A61rMv6hh+mngbeUOzczMpsNnipqZJcKBbmaWCAe6mVkiHOhmZolwoJuZJcKBbmaWCAe6mVkiHOhmZolwoJuZJcKBbmaWCAe6mVkiHOhmZolwoJuZJcKBbmaWCAe6mVkiHOhmZolwoJuZJSLPNUWXS/qxpK2Stkj6aIs2VUm7JG3Kbhe1WpeZmc2ePNcU3Q2cGxF3SToIGJN0a0T8sqndTyPi1PKHaGZmeXTcQ4+IByPirmz6CWArsGy2B2ZmZtOjiMjfWBoAbgOOiojHG+ZXgZuAbcAO4LyI2NKi/xAwBNDf379qeHi40KDHt+8q1K8MK5ctKdy3VqvR19dX4mjmtl6rF3qv5l6rF7pf8+Dg4FhEVFotyx3okvqAnwD/GhHfaVp2MPBsRNQknQx8MSJWTLW+SqUSo6OjuR672cC6jYX6lWHyklMK9x0ZGaFarZY3mDmu1+qF3qu51+qF7tcsqW2g5/qWi6RF1PfAv9kc5gAR8XhE1LLpW4BFkpbOYMxmZjZNeb7lIuAqYGtEfKFNm5dl7ZB0dLbeP5Q5UDMzm1qeb7kcB7wLGJe0KZv3CeBvACLiSuAM4GxJu4GngDUxnYPzZmY2Yx0DPSJ+BqhDmyuAK8oalJmZTZ/PFDUzS4QD3cwsEQ50M7NEONDNzBLhQDczS4QD3cwsEQ50M7NEONDNzBLhQDczS4QD3cwsEQ50M7NEONDNzBLhQDczS4QD3cwsEQ50M7NEONDNzBLhQDczS0Sea4oul/RjSVslbZH00RZtJOlLkiYkbZb0+tkZrpmZtZPnmqK7gXMj4i5JBwFjkm6NiF82tDkJWJHdjgG+kv01M7N9pOMeekQ8GBF3ZdNPAFuBZU3NTgeujbrbgUMkHVr6aM3MrC1FRP7G0gBwG3BURDzeMP9m4JLsgtJI+iFwfkSMNvUfAoYA+vv7Vw0PDxca9Pj2XYX6lWHlsiWF+9ZqNfr6+koczdzWa/VC79U8n+stmiP9B8BDT83ssWeSI4ODg2MRUWm1LM8hFwAk9QE3AR9rDPM9i1t02et/iohYD6wHqFQqUa1W8z7886xdt7FQvzJMnlkt3HdkZISiNc9HvVYv9F7N87neojly7srdXDaeOzpbmkmOTCXXt1wkLaIe5t+MiO+0aLINWN5w/zBgx8yHZ2ZmeeX5louAq4CtEfGFNs02AO/Ovu1yLLArIh4scZxmZtZBnvcNxwHvAsYlbcrmfQL4G4CIuBK4BTgZmAD+BLyn/KGamdlUOgZ69kFnq2PkjW0C+FBZgzIzs+nzmaJmZolwoJuZJcKBbmaWCAe6mVkiHOhmZolwoJuZJcKBbmaWCAe6mVkiHOhmZolwoJuZJcKBbmaWCAe6mVkiHOhmZolwoJuZJcKBbmaWCAe6mVkiHOhmZonIc03RqyU9LOmeNsurknZJ2pTdLip/mGZm1kmea4p+DbgCuHaKNj+NiFNLGZGZmRXScQ89Im4Ddu6DsZiZ2Qyofn3nDo2kAeDmiDiqxbIqcBOwDdgBnBcRW9qsZwgYAujv7181PDxcaNDj23cV6leGlcuWFO5bq9Xo6+srcTRzW6/VC71X83yut2iO9B8ADz01s8eeSY4MDg6ORUSl1bIyAv1g4NmIqEk6GfhiRKzotM5KpRKjo6MdH7uVgXUbC/Urw+QlpxTuOzIyQrVaLW8wc1yv1Qu9V/N8rrdojpy7cjeXjec5Wt3eTHJEUttAn/G3XCLi8YioZdO3AIskLZ3pes3MbHpmHOiSXiZJ2fTR2Tr/MNP1mpnZ9HR83yDpOqAKLJW0DfgksAggIq4EzgDOlrQbeApYE3mO45iZWak6BnpEvKPD8iuof63RzMy6yGeKmpklwoFuZpYIB7qZWSIc6GZmiXCgm5klwoFuZpYIB7qZWSIc6GZmiXCgm5klwoFuZpYIB7qZWSIc6GZmiXCgm5klwoFuZpYIB7qZWSIc6GZmiXCgm5klomOgS7pa0sOS7mmzXJK+JGlC0mZJry9/mGZm1kmePfSvAaunWH4SsCK7DQFfmfmwzMxsujoGekTcBuycosnpwLVRdztwiKRDyxqgmZnlo4jo3EgaAG6OiKNaLLsZuCQifpbd/yFwfkSMtmg7RH0vnv7+/lXDw8OFBj2+fVehfmVYuWxJ4b61Wo2+vr4SR7NvFH2++w+Ah54q/rgzea67Zb5u46Lmc73del3DzF7bg4ODYxFRabVsYeG1Pkct5rX8XyIi1gPrASqVSlSr1UIPuHbdxkL9yjB5ZrVw35GREYrW3E1Fn+9zV+7msvHiL7GZPNfdMl+3cVHzud5uva5h9l7bZXzLZRuwvOH+YcCOEtZrZmbTUEagbwDenX3b5VhgV0Q8WMJ6zcxsGjq+b5B0HVAFlkraBnwSWAQQEVcCtwAnAxPAn4D3zNZgzcysvY6BHhHv6LA8gA+VNiIzMyvEZ4qamSXCgW5mlggHuplZIhzoZmaJcKCbmSXCgW5mlggHuplZIhzoZmaJcKCbmSXCgW5mlggHuplZIhzoZmaJcKCbmSXCgW5mlggHuplZIhzoZmaJcKCbmSUiV6BLWi3pPkkTkta1WL5W0iOSNmW395c/VDMzm0qea4ouAL4M/AOwDfiFpA0R8cumptdHxDmzMEYzM8shzx760cBERPwmIv4MDAOnz+6wzMxsulS/xvMUDaQzgNUR8f7s/ruAYxr3xiWtBT4DPAL8Cvh4RDzQYl1DwBBAf3//quHh4UKDHt++q1C/MqxctqRw31qtRl9fX4mj2TeKPt/9B8BDTxV/3Jk8190yX7dxUfO53m69rmFmr+3BwcGxiKi0WtbxkAugFvOa/xf4L+C6iHhG0geAa4Dj9+oUsR5YD1CpVKJareZ4+L2tXbexUL8yTJ5ZLdx3ZGSEojV3U9Hn+9yVu7lsPM9LrLWZPNfdMl+3cVHzud5uva5h9l7beQ65bAOWN9w/DNjR2CAi/hARz2R3vwqsKmd4ZmaWV55A/wWwQtLhkvYH1gAbGhtIOrTh7mnA1vKGaGZmeXR83xARuyWdA3wfWABcHRFbJF0MjEbEBuAjkk4DdgM7gbWzOGYzM2sh14GgiLgFuKVp3kUN0xcAF5Q7NDMzmw6fKWpmlggHuplZIhzoZmaJcKCbmSXCgW5mlggHuplZIhzoZmaJcKCbmSXCgW5mlggHuplZIhzoZmaJcKCbmSXCgW5mlggHuplZIhzoZmaJcKCbmSXCgW5mlohcgS5ptaT7JE1IWtdi+WJJ12fL75A0UPZAzcxsah0DXdIC4MvAScCRwDskHdnU7H3AYxFxBHA5cGnZAzUzs6nl2UM/GpiIiN9ExJ+BYeD0pjanA9dk0zcCJ0hSecM0M7NO8lwkehnwQMP9bcAx7dpExG5Ju4AXA482NpI0BAxld2uS7isy6G7SzN57LKXpOUnZR2ZY7wyf627pqW1M79U749c1zPi1/fJ2C/IEeqs97SjQhohYD6zP8ZhJkjQaEZVuj2Nf6bV6ofdq7rV6YW7XnOeQyzZgecP9w4Ad7dpIWggsAXaWMUAzM8snT6D/Algh6XBJ+wNrgA1NbTYAZ2XTZwA/ioi99tDNzGz2dDzkkh0TPwf4PrAAuDoitki6GBiNiA3AVcDXJU1Q3zNfM5uDnsd67XBTr9ULvVdzr9ULc7hmeUfazCwNPlPUzCwRDnQzs0Q40AuQNClpXNImSaPZvBdJulXSr7O/L8zmS9KXsp9F2Czp9Q3rOStr/2tJZzXMX5WtfyLr29WTtNrU+zlJ92Y1fVfSIQ3tL8jGfp+kExvmt/wJiewD9zuy5+H67MP3rmpVc8Oy8ySFpKXZ/Xm/jbMxtaxZ0oez7bZF0mcb5s/r7dzmdf1aSbfvmSfp6Gz+/NjGEeHbNG/AJLC0ad5ngXXZ9Drg0mz6ZOB71L+rfyxwRzb/RcBvsr8vzKZfmC27E3hj1ud7wElzsN5/BBZm05c21HskcDewGDgcuJ/6h+kLsulXAPtnbY7M+twArMmmrwTOnovbOJu/nPoXBH63Z3kK23iK7TwI/DewOLv/0lS2c5t6f7BnW2TbdWQ+bWPvoZen8ecPrgHe2jD/2qi7HThE0qHAicCtEbEzIh4DbgVWZ8sOjoifR/1VcW3DuuaMiPhBROzO7t5O/fwEqNc7HBHPRMRvgQnqPx/R8icksr2W46n/ZAQ8/7mbiy4H/oXnnziX5DbOnA1cEhHPAETEw9n8VLdzAAdn00t47pybebGNHejFBPADSWOq/5wBQH9EPAiQ/X1pNr/VTycs6zB/W4v53dSq3kbvpb4HAtOv98XAHxv+c5gL9UKLmiWdBmyPiLub2qawjaH1dn4l8PfZoZKfSHpDNj+F7dyq3o8Bn5P0APB54IJs/rzYxnlO/be9HRcROyS9FLhV0r1TtG33swjTnd9Ne9UbEbcBSLoQ2A18M2vbbvytdh7mar3QehtfSP1QU7MUtjG0rnkh9UMJxwJvAG6Q9ArS2M6t6j0D+HhE3CTp7dTPsXkL82Qbew+9gIjYkf19GPgu9beZD2Vvs8j+7nlr2u6nE6aaf1iL+V3Tpl6yD4BOBc7M3lbC9Ot9lPrb14VN87uqRc1vpn6s+G5Jk9THeZekl5HANoa223kb8J3sUMOdwLPUf5xq3m/nNvWeBXwna/LtbB7Ml228rz6ASOUGHAgc1DD9P8Bq4HM8/0PRz2bTp/D8D1PujOc+TPkt9b2fF2bTL8qW/SJru+fDlJPnYL2rgV8CL2lq/2qe/2HZb6h/ULYwmz6c5z4se3XW59s8/8OyD87FbdzUZpLnPhSd19u4w3b+AHBxNv+V1A8vaL5v5ynq3QpUs/knAGPzaRt37QU0X2/UP72/O7ttAS7M5r8Y+CHw6+zvno0q6hcIuR8YByoN63ov9Q+TJoD3NMyvAPdkfa4gO6N3jtU7kf3j3pTdrmzoc2E29vto+GSf+jcFfpUtu7DpMe7M1vltsm9UzLWam9pM8lygz+tt3GE77w98IxvrXcDxKWznKep9EzCWzb8DWDWftrFP/TczS4SPoZuZJcKBbmaWCAe6mVkiHOhmZolwoJuZJcKBbmaWCAe6mVki/h+tahi2H3cheAAAAABJRU5ErkJggg==\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "grouped_df.hist(column=\"salary\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 128,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x153dfa34788>"
      ]
     },
     "execution_count": 128,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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Nt20cSMBnCTMzJpQz16bcN3ke5Y97+o2lTyubjIzs1xOEmZmlstJwszMcjlJmJk12Cc+8Qmm3HJj7Q2bgBuuzWy1M/AX23buG45f2Lnv10FdOe1GLU4SZmad4JVXXuHII4+kpaWFpUuXcsYZZ/DEE09w8803s2jRIvbYYw9+/vOfrzAn089++B3unnIbixcvYtCQ3TnjvB8giWOP+BC7DB7KjGkPMHTPvbj1N9fw5JNP0r17d1588UUGDhzIU089Rffu3bv0c7m6ycysE9x2221sueWWPPLII8yaNYuRI0dy0kkn8dBDDzFr1iwWLVrE73//+xX2GzPuOH51yx38ZuqfWbx4EXf94bZlr7304kImXn8LJ3zxFIYPH84tt2QLLV1zzTUcfvjhXZ4gwEnCzKxTDBgwgD/84Q+ccsop3HPPPfTo0YM777yT3XffnQEDBnDHHXfw2GOPrbDfQ3++h48dvB+H77cHD953D39/8m/LXtv/4I8se/ypT31q2VxMl156Kcccc0zXfyhc3WRm1il22GEHpk+fzqRJkzjttNMYMWIEF154IdOmTWPrrbdm/PjxLF68eLl9Xlu8mHO/8RWuvuUO3r5lXy76/nm8/tpry15ff4MNlj3ec889mTNnDnfddRdLly5l5513bsjn8pWEmVknmDt3LhtssAFHH300X/nKV3j44YcB6N27Ny+//DLXX3/9Cvu8lhJCz16b8uorL9fs8TR27FjGjBnTsKsI8JWEmVmnePTRR/nqV7/KWmutRffu3bnooov43e9+x4ABA+jXr9+yFesqbdyjB4ePGcuoD+7Jlltvw0677NruMT72sY9x+umnM2bMmK76GCtwkjCz1c7MT6242E9Xz320//77s//++y9XNmTIEM4555wVtr3sssuY2bIAgJO+djonfe30Fba55NcrNnLfe++9jBo1ip49GzePk5OEmVkJfO5zn+PWW29l0qTcpXy6hJOEmVkJ/PjHPy7kuG64NjOzXE4SZlZ6QRARRYdRCh39d3KSMLPS++eCN1jy6otOFDVEBC+88ALrrbde3fu4TcLMSu/HD8znc8C2PZ9HqOo2j7+0fmODquG/8xd1aPvOin+99dajb9++dW/vJGFmpffia29y7t0vtLvNnPMOalA09Tng1Fs6tH1R8bu6yczMcjlJmJlZLicJMzPL5SRhZma5nCTM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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "grouped_df.plot.bar()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "anaconda-cloud": {},
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  },
  "varInspector": {
   "cols": {
    "lenName": 16,
    "lenType": 16,
    "lenVar": 40
   },
   "kernels_config": {
    "python": {
     "delete_cmd_postfix": "",
     "delete_cmd_prefix": "del ",
     "library": "var_list.py",
     "varRefreshCmd": "print(var_dic_list())"
    },
    "r": {
     "delete_cmd_postfix": ") ",
     "delete_cmd_prefix": "rm(",
     "library": "var_list.r",
     "varRefreshCmd": "cat(var_dic_list()) "
    }
   },
   "types_to_exclude": [
    "module",
    "function",
    "builtin_function_or_method",
    "instance",
    "_Feature"
   ],
   "window_display": false
  }
 },
 "nbformat": 4,
 "nbformat_minor": 1
}
