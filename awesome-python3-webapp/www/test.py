#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import orm
from models import User,Blog,Comment
import asyncio

async def test(loop):
    await orm.create_pool(loop=loop,user='root',password='19921108',db='awesome')
    u=User(name='test',email='test@example.com',passwd='123456789',image='about:blank',admin=1,)
    await u.save()

loop=asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()


