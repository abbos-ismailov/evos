from typing import Union

import asyncpg
from asyncpg import Connection
from asyncpg.pool import Pool

from data import config


class Db_connect:

    def __init__(self):
        self.pool: Union[Pool, None] = None

    async def create(self):
        self.pool = await asyncpg.create_pool(
            user=config.DB_USER,
            password=config.DB_PASS,
            host=config.DB_HOST,
            database=config.DB_NAME
        )

    async def execute(self, command, *args,
                      fetch: bool = False,
                      fetchval: bool = False,
                      fetchrow: bool = False,
                      execute: bool = False
                      ):
        async with self.pool.acquire() as connection:
            connection: Connection
            async with connection.transaction():
                if fetch:
                    result = await connection.fetch(command, *args)
                elif fetchval:
                    result = await connection.fetchval(command, *args)
                elif fetchrow:
                    result = await connection.fetchrow(command, *args)
                elif execute:
                    result = await connection.execute(command, *args)
            return result

    async def create_table_users(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Users (
        user_id SERIAL PRIMARY KEY,
        user_tg_id BIGINT NOT NULL UNIQUE,
        full_name VARCHAR(255) NOT NULL,
        username VARCHAR(255) NULL,
        phone VARCHAR(60)
        );
        """
        await self.execute(sql, execute=True)

    async def create_table_foods(self):
        sql = """
        CREATE TABLE IF NOT EXISTS foods (
        food_id SERIAL NOT NULL,
        food_name VARCHAR(300) NOT NULL,
        food_price VARCHAR(255) NULL,
        food_url VARCHAR(960),
        food_type VARCHAR(120)
        );
        """
        await self.execute(sql, execute=True)

    async def create_table_ordered_foods(self):
        sql = """
        CREATE TABLE IF NOT EXISTS ordered_foods (
        user_tg_id BIGINT NOT NULL,
        food_id INT NOT NULL,
        food_name VARCHAR(300) NOT NULL,
        food_price VARCHAR(255) NULL,
        food_url VARCHAR(960),
        food_type VARCHAR(120),
        food_count INT NOT NULL
        );
        """
        await self.execute(sql, execute=True)


    async def create_table_customers(self):
        sql = """
        CREATE TABLE IF NOT EXISTS customers (
        user_tg_id BIGINT NOT NULL,
        tg_username VARCHAR(250) NULL,
        full_name VARCHAR(300) NOT NULL,
        phone VARCHAR(255) NULL,
        location VARCHAR(360),
        orintir VARCHAR(820)
        );
        """
        await self.execute(sql, execute=True)
    
    
    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ${num}" for num, item in enumerate(parameters.keys(), start=1)
        ])
        return sql, tuple(parameters.values())

    async def add_user(self, telegram_id, full_name, telephone, username):
        sql = """
        INSERT INTO Users(user_tg_id, full_name, username, phone) VALUES($1, $2, $3, $4) returning *
        """
        return await self.execute(sql, telegram_id, full_name, telephone, username, fetchrow=True)

    async def get_one_user(self, **kwargs):
        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return await self.execute(sql, *parameters, fetchrow=True)

    # FOODS table
    async def add_food(self, food_name, food_price, food_url, food_type):
        sql = """
        INSERT INTO foods(food_name, food_price, food_url, food_type) VALUES($1, $2, $3, $4) returning *
        """
        return await self.execute(sql, food_name, food_price, food_url, food_type, fetchrow=True)

    async def delete_food(self, food_id):
        await self.execute("DELETE FROM foods WHERE food_id=$1", food_id, execute=True)

    async def show_foods(self, food_type):
        return await self.execute("SELECT * FROM foods WHERE food_type=$1", food_type, fetch=True)

    async def update_price(self, new_price, food_id):
        return await self.execute("UPDATE foods SET food_price=$1 WHERE food_id=$2", new_price, food_id, execute=True)

    async def get_one_food(self, food_id):
        sql = "SELECT * FROM foods WHERE food_id=$1"
        return await self.execute(sql, food_id, fetchrow=True)

    # ORDERED_FOODS TABLE functions
    async def insert_food_to_orders(self, user_tg_id, food_id, food_name, food_price, food_url, food_type, food_count):
        sql = """
        INSERT INTO ordered_foods(user_tg_id, food_id, food_name, food_price, food_url, food_type, food_count) VALUES($1, $2, $3, $4, $5, $6, $7) returning *
        """
        return await self.execute(sql, user_tg_id, food_id, food_name, food_price, food_url, food_type, food_count, fetchrow=True)

    async def show_korzinka(self, user_tg_id):
        return await self.execute("SELECT * FROM ordered_foods WHERE user_tg_id=$1", user_tg_id, fetch=True)
    
    async def delete_korzinka(self, user_tg_id):
        await self.execute("DELETE FROM ordered_foods WHERE user_tg_id=$1", user_tg_id, execute=True)
    
    async def select_food_from_ordered_foods(self, food_id):
        sql = "SELECT * FROM ordered_foods WHERE food_id=$1"
        return await self.execute(sql, food_id, fetchrow=True)
    
    async def delete_foods_from_korzinka(self, user_tg_id):
        await self.execute("DELETE FROM ordered_foods WHERE user_tg_id=$1", user_tg_id, execute=True)
    
    
    ### CUSTOMERS table
    async def add_to_customers(self, user_tg_id, tg_username, full_name, phone, location, orintir):
        sql = """
        INSERT INTO customers(user_tg_id, tg_username, full_name, phone, location, orintir) VALUES($1, $2, $3, $4, $5, $6) returning *
        """
        return await self.execute(sql, user_tg_id, tg_username, full_name, phone, location, orintir, fetchrow=True)
    
    async def show_customers(self):
        return await self.execute("SELECT * FROM customers ",  fetch=True)

    async def delete_customer(self, user_tg_id):
        await self.execute("DELETE FROM customers WHERE user_tg_id=$1", user_tg_id, execute=True)