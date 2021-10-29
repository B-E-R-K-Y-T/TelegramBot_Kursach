toc.dat                                                                                             0000600 0004000 0002000 00000010071 14137066346 0014450 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        PGDMP       "    3             	    y            KURSACH    13.4    13.4     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false         �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false         �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false         �           1262    32778    KURSACH    DATABASE     f   CREATE DATABASE "KURSACH" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'Russian_Russia.1251';
    DROP DATABASE "KURSACH";
                postgres    false         �            1259    32795    ai    TABLE     ^   CREATE TABLE public.ai (
    id integer,
    id_message integer,
    dialogs text NOT NULL
);
    DROP TABLE public.ai;
       public         heap    postgres    false         �            1259    32842    messages    TABLE     �   CREATE TABLE public.messages (
    id integer,
    id_message integer NOT NULL,
    id_users integer,
    user_name text,
    dialogs text
);
    DROP TABLE public.messages;
       public         heap    postgres    false         �            1259    32829    usr    TABLE     _   CREATE TABLE public.usr (
    id integer,
    id_message integer,
    dialogs text NOT NULL
);
    DROP TABLE public.usr;
       public         heap    postgres    false         �          0    32795    ai 
   TABLE DATA           5   COPY public.ai (id, id_message, dialogs) FROM stdin;
    public          postgres    false    200       2998.dat �          0    32842    messages 
   TABLE DATA           P   COPY public.messages (id, id_message, id_users, user_name, dialogs) FROM stdin;
    public          postgres    false    202       3000.dat �          0    32829    usr 
   TABLE DATA           6   COPY public.usr (id, id_message, dialogs) FROM stdin;
    public          postgres    false    201       2999.dat ,           2606    32802 
   ai ai_pkey 
   CONSTRAINT     M   ALTER TABLE ONLY public.ai
    ADD CONSTRAINT ai_pkey PRIMARY KEY (dialogs);
 4   ALTER TABLE ONLY public.ai DROP CONSTRAINT ai_pkey;
       public            postgres    false    200         0           2606    32849    messages messages_pkey 
   CONSTRAINT     \   ALTER TABLE ONLY public.messages
    ADD CONSTRAINT messages_pkey PRIMARY KEY (id_message);
 @   ALTER TABLE ONLY public.messages DROP CONSTRAINT messages_pkey;
       public            postgres    false    202         .           2606    32836    usr usr_pkey 
   CONSTRAINT     O   ALTER TABLE ONLY public.usr
    ADD CONSTRAINT usr_pkey PRIMARY KEY (dialogs);
 6   ALTER TABLE ONLY public.usr DROP CONSTRAINT usr_pkey;
       public            postgres    false    201         2           2606    32850    messages messages_dialogs_fkey    FK CONSTRAINT        ALTER TABLE ONLY public.messages
    ADD CONSTRAINT messages_dialogs_fkey FOREIGN KEY (dialogs) REFERENCES public.ai(dialogs);
 H   ALTER TABLE ONLY public.messages DROP CONSTRAINT messages_dialogs_fkey;
       public          postgres    false    2860    200    202         3           2606    32855    messages messages_dialogs_fkey1    FK CONSTRAINT     �   ALTER TABLE ONLY public.messages
    ADD CONSTRAINT messages_dialogs_fkey1 FOREIGN KEY (dialogs) REFERENCES public.usr(dialogs);
 I   ALTER TABLE ONLY public.messages DROP CONSTRAINT messages_dialogs_fkey1;
       public          postgres    false    202    2862    201         1           2606    32837    usr usr_dialogs_fkey    FK CONSTRAINT     u   ALTER TABLE ONLY public.usr
    ADD CONSTRAINT usr_dialogs_fkey FOREIGN KEY (dialogs) REFERENCES public.ai(dialogs);
 >   ALTER TABLE ONLY public.usr DROP CONSTRAINT usr_dialogs_fkey;
       public          postgres    false    201    2860    200                                                                                                                                                                                                                                                                                                                                                                                                                                                                               2998.dat                                                                                            0000600 0004000 0002000 00000000005 14137066346 0014272 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        \.


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           3000.dat                                                                                            0000600 0004000 0002000 00000000005 14137066346 0014241 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        \.


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           2999.dat                                                                                            0000600 0004000 0002000 00000000005 14137066346 0014273 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        \.


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           restore.sql                                                                                         0000600 0004000 0002000 00000007377 14137066346 0015414 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        --
-- NOTE:
--
-- File paths need to be edited. Search for $$PATH$$ and
-- replace it with the path to the directory containing
-- the extracted data files.
--
--
-- PostgreSQL database dump
--

-- Dumped from database version 13.4
-- Dumped by pg_dump version 13.4

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

DROP DATABASE "KURSACH";
--
-- Name: KURSACH; Type: DATABASE; Schema: -; Owner: postgres
--

CREATE DATABASE "KURSACH" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'Russian_Russia.1251';


ALTER DATABASE "KURSACH" OWNER TO postgres;

\connect "KURSACH"

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: ai; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.ai (
    id integer,
    id_message integer,
    dialogs text NOT NULL
);


ALTER TABLE public.ai OWNER TO postgres;

--
-- Name: messages; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.messages (
    id integer,
    id_message integer NOT NULL,
    id_users integer,
    user_name text,
    dialogs text
);


ALTER TABLE public.messages OWNER TO postgres;

--
-- Name: usr; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.usr (
    id integer,
    id_message integer,
    dialogs text NOT NULL
);


ALTER TABLE public.usr OWNER TO postgres;

--
-- Data for Name: ai; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.ai (id, id_message, dialogs) FROM stdin;
\.
COPY public.ai (id, id_message, dialogs) FROM '$$PATH$$/2998.dat';

--
-- Data for Name: messages; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.messages (id, id_message, id_users, user_name, dialogs) FROM stdin;
\.
COPY public.messages (id, id_message, id_users, user_name, dialogs) FROM '$$PATH$$/3000.dat';

--
-- Data for Name: usr; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.usr (id, id_message, dialogs) FROM stdin;
\.
COPY public.usr (id, id_message, dialogs) FROM '$$PATH$$/2999.dat';

--
-- Name: ai ai_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ai
    ADD CONSTRAINT ai_pkey PRIMARY KEY (dialogs);


--
-- Name: messages messages_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.messages
    ADD CONSTRAINT messages_pkey PRIMARY KEY (id_message);


--
-- Name: usr usr_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.usr
    ADD CONSTRAINT usr_pkey PRIMARY KEY (dialogs);


--
-- Name: messages messages_dialogs_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.messages
    ADD CONSTRAINT messages_dialogs_fkey FOREIGN KEY (dialogs) REFERENCES public.ai(dialogs);


--
-- Name: messages messages_dialogs_fkey1; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.messages
    ADD CONSTRAINT messages_dialogs_fkey1 FOREIGN KEY (dialogs) REFERENCES public.usr(dialogs);


--
-- Name: usr usr_dialogs_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.usr
    ADD CONSTRAINT usr_dialogs_fkey FOREIGN KEY (dialogs) REFERENCES public.ai(dialogs);


--
-- PostgreSQL database dump complete
--

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 