def start(p):
	p.enemy_rows=0
	p.enemy_cols=0
	p.enemyodds=100
	for player in p.playermanager:
		player.change_gun("Gun","TestingBullet",p.playerbulletmanager)
