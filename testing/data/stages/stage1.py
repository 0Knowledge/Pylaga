def start(p):
	p.enemy_rows=7
	p.enemy_cols=7
	p.enemyodds=100
	for player in p.playermanager:
		player.change_gun("SwarmGun","Swarm",p.playerbulletmanager)
