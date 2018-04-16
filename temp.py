def jeu():



    vie = 3
    print ("debut:", vie)


    # fenetre.blit(poulpe.getPoulpe(), (200,300))    ?

    # Création de la liste des invaders

      # verts


    # creation de l'invader bonus
    list_bonus = []

    def bonus():
        list_bonus.append(Bonus(pygame, x, y))
        for i in range(len(list_bonus)):
            i.allerAgauche()
            x_b = i.getX()
            if x_b < -20:
                list_bonus.remove(i)

    def tempo():
        t = Timer(200, bonus)
        t.start()













    pygame.display.flip()  # rafraichissement de l'image pour faire apparaitre les invaders, le poulpe et le fond

    # score
    # score = Score('Leo')
    # score.ajouterPoint()
    # print(score.recupererPoint())

    # creation  d'un boucle infinie pour que le jeu ne se ferme pas
    continuer = 1

    # pygame.key.set_repeat(1,10) #on defini l'affichage d'une image toutes les 10ms
    stop_invaders_a_droite = False
    stop_invaders_a_gauche = True

    while continuer:
        temps = pygame.time.get_ticks()  # essais sur le temps pour invaders bonus + projectiles espacés + poulpe qui disparait quand il se fait touché
        for event in pygame.event.get():  # on parcours la liste de tous les évènements pouvant être reçus
            if event.type == QUIT:  # si l'évènement est de type QUIT (on clique sur la croix)
                continuer = 0  # on arrête la boucle

            if event.type == KEYDOWN:  # si une touche du clavier est pressée
                if event.key == K_LEFT:  # Lorsque l'on va appuyer sur la flèche de gauche
                    poulpe.allerAgauche()  # Le poulpe va se déplacer de 5px vers la gauche

                if event.key == K_RIGHT:  # Lorsque l'on va appuyer sur la flèche de droite
                    poulpe.allerAdroite()  # Le poulpe va se déplacer de 5px vers la droite

                if event.key == K_ESCAPE:
                    continuer = 0

                if event.key == K_SPACE:
                    x = poulpe.getX()
                    y = poulpe.getY()
                    if len(list_tirs) == 0:
                        ajouter_tir(x, y)

        # pygame.display.flip
        collision_tir_invaders()
        collision_tir_poulpe()
        tempo()
        # on affiche les tirs des invaders
        for i in range(len(list_tirs_inv)):
            fenetre.blit(list_tirs_inv[i].getTir(),
                         list_tirs_inv[i].getPosition())  # collage de l'image et de la position de chaque tir


        if collision() or vie == 0:

            print vie
            pygame.mixer.music.stop()  # La musique s'arrete
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        jeu()


        elif len(list_invaders) == 0:
            fenetre.blit(fond_gagne, (0, 0))  # on recolle le fond
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        continuer = 0


        else:











            # si le poulpe est touché par un tir, il perd une vie
            if collision_tir_poulpe():
                vie = vie - 1
                print vie

                # set_timer(Bonus(), 3000)
            # pygame.time.set_timer(bonus, 3000)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()


jeu()
