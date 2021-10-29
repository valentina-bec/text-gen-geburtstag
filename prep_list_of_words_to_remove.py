# -*- coding: utf-8 -*-

import pickle


list_of_replacement = ['(',')','Albert','Schweizer', 'Joachim','Ringelnatz','Klassisch','Wolf','Dietrich' ,'Matthias','Claudius',
                           'Franz','Grillparzer', 'Allgemein', 'Amalia','von Wendlingen','Uta','Jeschker', 'Karel','Čapek',
                           'Johann','Wolfgang','von Goethe', 'Alitirischer', 'Segenswunsch', 'Friedrich Ast', 'Eduard','Möricke','Unbekannt',
                      'Jole','von Weißenberg', 'Rainer','Maria Rilke', 'Modern','Frank','von Schillerberg-Gosheim',
                       'Seite_2','__eine_der_umfangreichsten_Sammlungen_im_Netz.txt|','"Friedrich','von Schiller', 'Konfuzius',
                       'Seite_3','__die_umfangreiche_Sammlung.txt|','"Altirischer',' Ralph Waldo Emerson', 'Adlai E.','Stevenson',
                       'Seite_3','__die_umfangreiche_Sammlung_im_Netz.txt|"Frank von Schillerberg-Gosheim','Jean de la Bruyère',
                       'Seite_4','__die_umfangreiche_Sammlung.txt|','"Friedrich Ast','Seite_5',
                       '__die_umfangreiche_Sammlung_im_Netz.txt|"Alter Trinkspruch','Ferdinand','von Saar',
                       'C. Goßmann', 'Friedrich','Morgenroth','Wilhelm','Busch',' Fontane','Christian','Morgenstern'
                       'Friedrich Rückert', 'Wolfgang','Goethe','- Lebensregel', 'Theodor','Storm', 'Kurt','Tucholsky',
                       'Ludwig','Pfau', 'Fred','Endrikat', 'August','Heinrich','Hoffmann von Fallersleben', 'Julius','Karl','Reinhold Sturm',
                       'R. Emerson','William','Shakespeare', 'Oscar','Wilde', 'Bettina','von Arnim', 'Peter','Rosegger', 'H. David Thoreau'
                       'Wilhelm','Raabe', 'Luther','Burbank','Carl','Hilty','Cesare','Pavese','Romano','Guardini', 'Andre','Maurois',
                       'Nicolas','Boileau-Despreaux','Jonathan','Swift','Franz','Kafka','Martin','Buber','Martina','Navratilova',
                       'Chinesisches','Sprichwort','J. W.','von Goethe','Tolstoi','Fernand','Gregh', 'Adalbert','Stifter',
                        'Als Beigabe zu Dessous gedacht)',
                       'S. Tucker','Udo','Hahn','Volkstümlich','Selma','Lagerlöf','C. Schwarz','Volksgut','Plutarch',
                       'Marie','von Ebner-Eschenbach','Antoine','de Saint-Exupéry', 'Vincent','van Gogh', 'H. David','Thoreau','Arabisches','Sprichwort',
                       'Jean','Paul', 'Wilhelm','Raabe','Japanische Weisheit','Sprichwort','Friedrich','Rückert', 'Otto','Riethmüller','Mark','Twain',
                       'Jean-Jacques Rousseau','Henry David Thoreau','Arthur Schopenhauer','Friedrich','Schiller','Erich Kästner','Nicolas','Boileau-Despréaux',
                       'Deutsches','Wold Dietrich', 'Charles de Montesquieu','Heinrich Heine','Anatole France','Irischer Segenswunsch',
                       'Altirischer Segenswunsch','Robert','Musil','Friedrich','Martin','von Bodenstedt','Georg',' Rudolf','Weckherlin',
                       'Ali','Ibn','Al Andalusi','Hazm','Volksmund','Rudolf','Baumbach','Cäsar','Otto','Flaischlen', 'Alois','Wohlmuth',
                       'Cäsar','Otto','Flaischlen','Friedrich','von Schiller','Ludwig','Eichrodt','Friedrich','Hölderlin','Johann','Georg Fischer',
                       'Jacques','Benigne Bossuet', 'Jean','Cocteau','Olga','Tschechowa','Truman','Capote','Leonie','Lars und Paul','Kurt','Beate und Peter',
                       'Anja, Nina und Doris','Hanna und Thomas','Manuela,','Silke und Johann','Helga,','Tonja und Martina','Nora und Katja',
                       'Viola,','Ben und','Daniel','Simone,','Christian,','Alex und Kai','Elke','Tanja,','Steffen und Moritz','Rolf','Marcel,','Sven und Sascha',
                       'Benjamin','Truck Stop','George','Eliot','Aus Englang','Otto','von Bismarck','Marc','Aurel','Klaus','Klages','Dagmar','Walther',
                       'Curd','Jürgens','Paul','Claudel','Alfred de Musset','Johann Nepumuk','Nestroy','S. Schwarz','Peter','Silie','Burkhard','Heidenberger',
                       'Unterschrift','Deutsches', 'Irisches','Oliver Wendell Holmes, US-amerikanischer Arzt, –', 'Maurice Chevalier, franz. Schauspieler,–',
                       'Bob Hope,','US-amerikanischer Komiker,','Pablo Casals,','span. Cellist, –',', engl. Dichter, 1564–1616','Alexis','Carrel,','franz. Physiologe, –',
                       'Ingmar','Bergman, schwed. Regisseur, –',', US-amerik. Schriftsteller, –',', österr. Schriftsteller, –','Englisches ',
                        'Francois','La Rochefoucauld','Bibel 14,14','Alfred','de Musset','Nikolaus','Lenau','Mahatma','Ghandi','Marc','Aurel','Otto','Ludwig',
                       'Diogenes','von Sinope','Aus','Norwegen','Cicero','Johannes','Trojan','Aus Ägypten','Afrikanische Weisheit','der Swahili',
                       'Truman','Capote','Leo','Daniel','Spitzer','Benjamin','Franklin','Johann','Anton Leisewitz','Aus Ägypten','Erasmus','von Rotterdam',
                       'Fjodor','Michailowitsch','Dostojewski','Clemens','Brentano','Heinrich','Martin','Otto','von Leixner','Carmen','Sylva','Irischer',' Segenswunsch',
                       'Agnes und Reihnhold','Gitta,','Margret,','Willi und Anton', 'Mona und Walter','Eduard Mörike','Carmen,','Ilona und Ingrid',
                       'Daniela und Mario','Deine Freundin Ute', 'Agnes und Reihnhold', 'Gitta,','Margret,','Willi und Anton',
                       'Frank und Rolf', 'Meike und Larissa','Michaela','Gabi,',' Ulrike und Peter','Joan','Collins','William','Somerset Maugham',
                       'Sven,','Walter und','David','Bob Hope','Sabrina und Benjamin','Johanna und Torben','Ute,','Petra, Ingolf und Karl',
                       'Nadine,','Martin und Dennis','Franziska','Doris','Weisheit aus Italien','Miriam und Andreas','Lena und Florian','Judit',
                       'Samuel Butler)','Renate,','Ida, Herbert und Hans','Dieter','Inge, Paula und Gabi','Jochen, Timo und Sven','Simone',
                       'Dein Thomas','Tante Ulrike','Manuela,','Lothar und Hans','Christian','Morgenstern','Ephraim','Kishon',
                       'Sabrina und','Deinen Kegelfreunden','Ernst','Thälmann','Christoph','Wilhelm von Hufeland','Deine Wanderfreunde',
                       'von Deinen Kumpels','Cäsar','Flaischlen','Alter Trinkspruch','Voltaire','Sören','Kierkegaard','Talmud','Paul','Heyse',
                       'Emanuel','Geibel','Daniel','Francois','Esprit Auber','Eduard','Mörike','Alexis','Carrel','Cäsar','Flaischlen','Deiner Patentante','Celina',
                       'Andrea','und Florian','Klara','Alina, Luisa und Denise','Dein Alfred','Margret, Matthias, Rudi und Phillip','George Clooney',
                       'Albert','Einstein','Abraham','Lincoln','Maurice','Chevalier, franz. Schauspieler,','Pablo','Casals, span. Cellist,','Alexis','Carrel, franz. Physiologe, ',
                       'Ingmar','Bergman, schwed. Regisseur, ',', US-amerik. Schriftsteller, ',', österr. Schriftsteller,','Xenophon','Samuel','Goldwyn',
                       'Horaz','Lateinisches','Alexander','von Humboldt',' Franklin', 'Russisches','Alter Trinkspruch','Georg Christoph Lichtenberg',
                       'Paul','Fleming','Emily','Dickinson','Alexis','Carrel','Otto','Fürst von Bismarck','Abraham','Gotthelf','Kästner','Friedrich','Schleiermacher',
                       'Martin','Luther','Cäsar','Flaischlen','Alter Trinkspruch','Aus Japan','Text kopieren Bild verschicken alle Bilder anzeigen',
                       'Gastbeitrag','Seite 2','myGratulations','Jole von','Weißenstein','Gotthold','Ephraim','Lessing','Kartenspruch','Epikur',
                       'Seigneur','Michel','Eyquem','de Montaigne','Neudeutsch', 'Happy Birthday', 'Cornelia','Sander','Klaus','Enser-Schlag',
                       'Anita','Menger','Monika','Minder','final', 'Oliver Wendell Holmes, US-amerikanischer Arzt','M. L Engle',
                       'de Saint-Exupèry','Text kopieren Bild verschicken  alle Bilder anzeigen', 'Beate und Man', 'e Clooney',
                       ' e Bernard Shaw','Pau Casals','Evelyn Waugh ', 'Ina Deter','Charles Dickens','Schweitzer',
                       'Arthur Schopenhauser ', 'Japanisches','Butler', 'Pearl Sydenstricker Buc','Charly Chaplin',
                       'Erich Maria Remarque','Wasilij Rosanow','Madame de Staël','Johnathan','Bergman',
                       'Chevalier','Farkas','Vivian Leigh','Gustav Knuth','Hebbel','Anthony Quinn',
                       'Katherine Hepburn','Curt Goetz','Lembke','von Hufeland','Chevalier','J.   Getty',' G. Laub',
                       'F. Rosay','Spanisches','Bonhoeffer','Rabelais ','Ägypten','J. Viktor von Scheffel',' Pearl S. Buck',
                       'Jules Romains','J. Harris','der Lebensregel von Baltimore','Jüdisches', ' Alter Liedtext',
                        'Tieck','Tertullian''gang von Goehte','Gottfried',' Heine','P. Rosenthal']

list_of_years = []
for i in range(1800, 2020):
    year = i
    list_of_years.append(year)
    list_of_replacement.append(year)

list_of_Geburtstagszitat = []
for i in range(1, 11):
    Geburtstagszitat = str(i)+' – Geburtstagszitat'
    list_of_replacement.append(Geburtstagszitat)

list_of_Geburtstagsspruch = []
for i in range(1, 13):
    Geburtstagsspruch = str(i)+' – Geburtstagsspruch'
    list_of_replacement.append(Geburtstagsspruch)

whole_list = []
whole_list.append(list_of_Geburtstagsspruch)
whole_list.append(list_of_Geburtstagszitat)
whole_list.append(list_of_years)
whole_list.append(list_of_replacement)

with open(r'removed_words.txt','wb') as file:
    pickle.dump(list_of_replacement, file)

print ('=======')
    #file.close()
with open(r'\removed_words.txt', 'rb') as file:
    words_to_remove = pickle.load(file)
    print(len(words_to_remove), "words to remove")


    file.close()
