PGDMP          /             	    y            KURSACH    13.4    13.4     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    32778    KURSACH    DATABASE     f   CREATE DATABASE "KURSACH" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'Russian_Russia.1251';
    DROP DATABASE "KURSACH";
                postgres    false            �            1259    32795    ai    TABLE     ^   CREATE TABLE public.ai (
    id integer,
    id_message integer,
    dialogs text NOT NULL
);
    DROP TABLE public.ai;
       public         heap    postgres    false            �            1259    32842    messages    TABLE     �   CREATE TABLE public.messages (
    id integer,
    id_message integer NOT NULL,
    id_users integer,
    user_name text,
    dialogs text
);
    DROP TABLE public.messages;
       public         heap    postgres    false            �            1259    32829    usr    TABLE     _   CREATE TABLE public.usr (
    id integer,
    id_message integer,
    dialogs text NOT NULL
);
    DROP TABLE public.usr;
       public         heap    postgres    false            �          0    32795    ai 
   TABLE DATA           5   COPY public.ai (id, id_message, dialogs) FROM stdin;
    public          postgres    false    200   a       �          0    32842    messages 
   TABLE DATA           P   COPY public.messages (id, id_message, id_users, user_name, dialogs) FROM stdin;
    public          postgres    false    202   ~       �          0    32829    usr 
   TABLE DATA           6   COPY public.usr (id, id_message, dialogs) FROM stdin;
    public          postgres    false    201   �       ,           2606    32802 
   ai ai_pkey 
   CONSTRAINT     M   ALTER TABLE ONLY public.ai
    ADD CONSTRAINT ai_pkey PRIMARY KEY (dialogs);
 4   ALTER TABLE ONLY public.ai DROP CONSTRAINT ai_pkey;
       public            postgres    false    200            0           2606    32849    messages messages_pkey 
   CONSTRAINT     \   ALTER TABLE ONLY public.messages
    ADD CONSTRAINT messages_pkey PRIMARY KEY (id_message);
 @   ALTER TABLE ONLY public.messages DROP CONSTRAINT messages_pkey;
       public            postgres    false    202            .           2606    32836    usr usr_pkey 
   CONSTRAINT     O   ALTER TABLE ONLY public.usr
    ADD CONSTRAINT usr_pkey PRIMARY KEY (dialogs);
 6   ALTER TABLE ONLY public.usr DROP CONSTRAINT usr_pkey;
       public            postgres    false    201            2           2606    32850    messages messages_dialogs_fkey    FK CONSTRAINT        ALTER TABLE ONLY public.messages
    ADD CONSTRAINT messages_dialogs_fkey FOREIGN KEY (dialogs) REFERENCES public.ai(dialogs);
 H   ALTER TABLE ONLY public.messages DROP CONSTRAINT messages_dialogs_fkey;
       public          postgres    false    2860    200    202            3           2606    32855    messages messages_dialogs_fkey1    FK CONSTRAINT     �   ALTER TABLE ONLY public.messages
    ADD CONSTRAINT messages_dialogs_fkey1 FOREIGN KEY (dialogs) REFERENCES public.usr(dialogs);
 I   ALTER TABLE ONLY public.messages DROP CONSTRAINT messages_dialogs_fkey1;
       public          postgres    false    202    2862    201            1           2606    32837    usr usr_dialogs_fkey    FK CONSTRAINT     u   ALTER TABLE ONLY public.usr
    ADD CONSTRAINT usr_dialogs_fkey FOREIGN KEY (dialogs) REFERENCES public.ai(dialogs);
 >   ALTER TABLE ONLY public.usr DROP CONSTRAINT usr_dialogs_fkey;
       public          postgres    false    201    2860    200            �      x������ � �      �      x������ � �      �      x������ � �     