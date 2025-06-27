import asyncio, asyncpg, json

from pydantic import BaseModel
from typing import Optional, List, Dict, Any

from data.config import database_config







class AsyncPostgresDB:
	def __init__(self):
		self.pool = None

	async def init_pool(self):
		self.pool = await asyncpg.create_pool(
			user=database_config['user'],
			password=database_config['password'],
			database=database_config['database_name'],
			host=database_config['host'],
			port=database_config['port']
		)
		await self.create_tables()

	async def close_pool(self):
		await self.pool.close()

	async def create_tables(self):
		async with self.pool.acquire() as conn:
			tables = {
				'users': '''
					CREATE TABLE IF NOT EXISTS users(
						id SERIAL PRIMARY KEY,
						tg_user_id BIGINT,
						tg_username TEXT,
						tg_firstname TEXT,
						referrer_from_user_id BIGINT REFERENCES users(id),
						created_at BIGINT
					)
				'''
			}

			for table in tables:
				await conn.execute(tables[table])


	async def execute(self, query: str, *args):
		async with self.pool.acquire() as conn:
			result = await conn.execute(query, *args)
		return result

	async def fetch(self, query: str, *args) -> List[Dict[str, Any]]:
		async with self.pool.acquire() as conn:
			result = await conn.fetch(query, *args)
		return [dict(record) for record in result]

	async def fetchrow(self, query: str, *args) -> Optional[Dict[str, Any]]:
		async with self.pool.acquire() as conn:
			result = await conn.fetchrow(query, *args)
		return dict(result) if result else None

	async def fetchval(self, query: str, *args) -> Optional[Any]:
		async with self.pool.acquire() as conn:
			result = await conn.fetchval(query, *args)
		return result

db = AsyncPostgresDB()