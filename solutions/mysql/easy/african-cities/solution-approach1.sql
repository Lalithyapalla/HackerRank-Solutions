-- ──────────────────────────────────────────────────
-- Problem     African Cities
-- Difficulty  Easy
-- Subdomain   Basic Join
-- Platform    HackerRank
-- Language    mysql
-- Status      Accepted
-- Submitted   2026-06-05, 03:07 p.m.
-- ──────────────────────────────────────────────────

select city.name 
from city,country
where city.countrycode=country.code and country.continent='Africa';
